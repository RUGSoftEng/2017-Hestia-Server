package peripherals;
import java.io.IOException;
import java.net.InetAddress;

public class Lock implements IPeripheral{
	private long id;
	
	private String ip;
	private String port;
	
	public Lock(String ip, String port, long id){
		this.id = id;
		this.ip = ip;
		this.port = port;
	}
	
	public Lock(InetAddress ip, int port, long id){
		this.ip = ip.toString();
		this.port = Integer.toString(port);
		this.id = id;
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
	
	private void sendCurl(String action) throws IOException, InterruptedException{
		Runtime runtime = Runtime.getRuntime();
		System.out.println(runtime.toString());
		
		String command = ip + ":" + port + "/arduino/" + action;
		Process process = runtime.exec("curl " + command );
		int resultCode = process.waitFor();
	
		if (resultCode != 0) {
		     // Sending the action didn't work
			// Perhaps create a special exception for this
			throw new IOException();
		} 

	}

	@Override
	public long getId() {
		return id;
	}

	@Override
	public String toString(){
		return ip + ":" + port;
	}

}
