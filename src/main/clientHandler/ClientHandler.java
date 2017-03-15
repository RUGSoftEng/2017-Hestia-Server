package clientHandler;

import messageExtractor.MessageJSONParser;
import messageExtractor.RequestManager;
import messageExtractor.UnexpectedActionException;
import peripherals.ActionNotDefinedException;
import peripherals.IPeripheral;
import peripherals.Lock;

import java.io.IOException;
import clientInteractors.ClientInteractor;
import peripheralDatabase.PeripheralDatabase;

/**
 * ClientHandler receives a string from a ClientInteractor. This string is 
 * parsed into a peripheral action. After this the thread is done.
 * @see Server
 */
public class ClientHandler implements Runnable{
    private ClientInteractor clientInteractor;
    private PeripheralDatabase peripheralDatabase;

    public ClientHandler(ClientInteractor clientInteractor, PeripheralDatabase database) {
        this.clientInteractor = clientInteractor;
        this.peripheralDatabase = database;
    }

    /**
     * The run method constantly tries to handle messages from the 
     * clientInteractor. It then sends a message to the peripheral based on the 
     * object that was sent as input.
     */
    @Override
    public void run() {
        
        RequestManager actionToPerform = null;
        try {
            actionToPerform = new MessageJSONParser().parseMessage(clientInteractor.getDataFromClient(), peripheralDatabase);
        } catch (UnexpectedActionException | IOException e) {
            e.printStackTrace();
            return;
        } finally {
            try {
                clientInteractor.stopInteracting();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        // TODO there should be a different architecture for adding peripherals, they should not be created here.
        String loopbackIp = "192.168.178.17";
        String tempPort = "80";
        IPeripheral target = new Lock(loopbackIp,tempPort);
        System.out.println(target);
        //System.out.println(actionToPerform.getAction());

        actionToPerform.handleMessage();
    }
}
