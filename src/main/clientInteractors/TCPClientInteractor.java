package clientInteractors;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * The TCPClientInteractor is a specific implementation of the ClientInteractor
 * interface. It works over TCP.
 * @see ClientInteractor
 */
public class TCPClientInteractor implements ClientInteractor {
    private static int port = 8000;
    private Socket clientSocket;

    /**
     * This method blocks until a connection can be accepted. 
     * @throws IOException 
     */
    @Override
    public void waitOnConnection() throws IOException {
            ServerSocket serverSocket = new ServerSocket(port);
            clientSocket =  serverSocket.accept();
            serverSocket.close();
    }

    /**
     * This method returns a message from the socket as a string.
     * We assume that an incoming message is self-contained on a single line.
     * @return a string to be used as a message by the ClientHandler class.
     * @throws IOException 
     */
    @Override
    public String getDataFromClient() throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        return in.readLine();
    }

    @Override
    public void sendDataToClient(String data) throws IOException {
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
        out.println(data);

    }

    @Override
    public void stopInteracting() throws IOException {
        clientSocket.close();
    }

    @Override
    public boolean isNotConnected() {
        return clientSocket == null;
    }


}
