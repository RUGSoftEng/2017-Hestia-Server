package clientInteractors;

import java.io.IOException;

/**
 * A ClientInteractor is able to get data from the client. Additionally, it is 
 * used by the server when waiting for a connection from the client.
 * @see TCPClientInteractor
 */
public interface ClientInteractor {
    void waitOnConnection() throws IOException;
    String getDataFromClient() throws IOException;
    void sendDataToClient(String data) throws IOException;
    void stopInteracting() throws IOException;
    boolean isNotConnected();
}
