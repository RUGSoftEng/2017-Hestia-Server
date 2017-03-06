import clientHandler.ClientHandlerThread;
import clientInteractors.ClientInteractorInterface;
import clientInteractors.TCPClientInteractor;

import java.io.IOException;

public class Server {

    public static void main(String[] args) {
	    runServer();
    }

    private static void runServer() {
        while(true){
            ClientInteractorInterface clientInteractor = setUpInteraction();
            try {
                new Thread(new ClientHandlerThread(clientInteractor.getDataFromClient())).start();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private static ClientInteractorInterface setUpInteraction() {
        ClientInteractorInterface interactor = new TCPClientInteractor();
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
