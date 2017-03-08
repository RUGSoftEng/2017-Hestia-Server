package clientInteractors;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Created by sebastian on 3/2/17.
 */
public class TCPClientInteractor implements ClientInteractorInterface {
    private static int port = 8000;
    private Socket clientSocket;

    @Override
    public void waitOnConnection() throws IOException {
            ServerSocket serverSocket = new ServerSocket(port);
            clientSocket =  serverSocket.accept();
            serverSocket.close();
    }

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
