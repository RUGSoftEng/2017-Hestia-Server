package peripherals;
import java.io.IOException;
import java.net.InetAddress;

/**
 * Implementation of the IPeripheral interface for the Lock peripheral. The lock works with
 * HTTP GET requests. 
 */
public class Lock implements IPeripheral{	
	private String ip;
	private String port;
	
	public Lock(String ip, String port){
		this.ip = ip;
		this.port = port;
	}
	
	public Lock(InetAddress ip, int port){
		this.ip = ip.toString();
		this.port = Integer.toString(port);
	}
	
	@Override
	public void performAction(String action) throws ActionNotDefinedException, IOException, InterruptedException{
		if(action.equals("openLock")){
			sendCurl("openlock");
		} else if(action.equals("closeLock")){
			sendCurl("closelock");
		} else { 
			throw new ActionNotDefinedException();
		}
	}
	
	/**
	 * This function sends the command to the peripheral using curl.
	 * @param action : The to perform action
	 * @throws IOException
	 * @throws InterruptedException
	 */
	private void sendCurl(String action) throws IOException, InterruptedException{
		Runtime runtime = Runtime.getRuntime();
		String command = ip + ":" + port + "/arduino/" + action;
		Process process = runtime.exec("curl " + command );
		int resultCode = process.waitFor();
	
		if (resultCode != 0) {
		    // Sending the action didn't work
			// Perhaps create a special exception for this
			throw new IOException();
		} 

	}
}
