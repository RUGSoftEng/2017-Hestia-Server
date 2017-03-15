import clientHandler.ClientHandler;
import clientInteractors.TCPClientInteractor;

import java.io.IOException;
import clientInteractors.ClientInteractor;

/**
 * This class contains the main functions on which the server depends.
 * It constantly listens for incoming messages. Upon receiving 
 * @see ClientHandler
 * @see ClientInteractor
 */

public class Server implements Runnable {

    public static void main(String[] args) {
	    new Server().run();
    }

    /**
     * The run method waits until a connection is established. After connecting
     * a new thread is created containing a handler. This new thread handles the
     * messages coming from the clientInteractor
     */
    public void run() {
        while(true){
            ClientInteractor clientInteractor = setUpInteraction();
            new ClientHandler(clientInteractor).run();
        }
    }

    /**
     * This method waits until a connection with a client is established through
     * TCP. 
     * @return An interactor object which can be used to obtain data from the 
     * client
     */
    private static ClientInteractor setUpInteraction() {
        ClientInteractor interactor = new TCPClientInteractor();
        while (interactor.isNotConnected()) {
            try {
                interactor.waitOnConnection();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return interactor;
    }
}
