package clientHandler;

import MessageExtractor.JSONExtractor;
import MessageExtractor.PeripheralAction;
import MessageExtractor.UnexpectedActionException;
import peripherals.ActionNotDefinedException;
import peripherals.IPeripheral;
import peripherals.Lock;

import java.io.IOException;

public class ClientHandlerThread implements Runnable{
    private String messageFromClient;

    public ClientHandlerThread(String dataFromClient) {
        messageFromClient = dataFromClient;
    }

    @Override
    public void run() {
        PeripheralAction actionToPerform = null;
        try {
            actionToPerform = new JSONExtractor().handleMessage(messageFromClient);
        } catch (UnexpectedActionException e) {
            e.printStackTrace();
        }
        // TODO Currently, we always get messages with id 1, change this to support multiple ids
        assert(actionToPerform != null && actionToPerform.getTargetId() == 1);

        // TODO there should be a different architecture for adding peripherals, they should not be created here.
        String loopbackIp = "127.0.0.1";
        String tempPort = "8800";
        IPeripheral target = new Lock(loopbackIp,tempPort,actionToPerform.getTargetId());
        System.out.println(target);
        System.out.println(actionToPerform.getAction());

        try {
            target.performAction(actionToPerform.getAction());
        } catch (ActionNotDefinedException | IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
