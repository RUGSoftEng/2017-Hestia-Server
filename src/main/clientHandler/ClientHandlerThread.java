package clientHandler;

import messageExtractor.JSONExtractor;
import messageExtractor.PeripheralAction;
import messageExtractor.UnexpectedActionException;
import clientInteractors.ClientInteractorInterface;
import peripherals.ActionNotDefinedException;
import peripherals.IPeripheral;
import peripherals.Lock;

import java.io.IOException;

public class ClientHandlerThread implements Runnable{
    private ClientInteractorInterface clientInteractor;

    public ClientHandlerThread(ClientInteractorInterface clientIntractor) {
        this.clientInteractor = clientIntractor;
    }

    @Override
    public void run() {
        PeripheralAction actionToPerform = null;
        try {
            actionToPerform = new JSONExtractor().handleMessage(clientInteractor.getDataFromClient());
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
        System.out.println(actionToPerform.getAction());

        try {
            target.performAction(actionToPerform.getAction());
        } catch (ActionNotDefinedException | IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
