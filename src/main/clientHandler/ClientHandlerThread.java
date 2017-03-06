package clientHandler;

import MessageExtractor.JSONExtractor;
import MessageExtractor.PeripheralAction;
import MessageExtractor.UnexpectedActionException;

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
        // Currently, we always get messages with id 1
        assert(actionToPerform != null && actionToPerform.getTargetId() == 1);
        performAction();
    }
}
