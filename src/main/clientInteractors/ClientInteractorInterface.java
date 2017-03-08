package clientInteractors;

import java.io.IOException;

/**
 * Created by sebastian on 3/2/17.
 */
public interface ClientInteractorInterface {
    void waitOnConnection() throws IOException;
    String getDataFromClient() throws IOException;
    void sendDataToClient(String data) throws IOException;
    void stopInteracting() throws IOException;
    boolean isNotConnected();
}
