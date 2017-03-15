package messageExtractor;

import peripheralDatabase.PeripheralDatabase;
import peripherals.IPeripheral;


public class ServerRequestManager extends RequestManager{
	private String request;
	
	public ServerRequestManager(String request, PeripheralDatabase database){
		super("request", database);
		this.request = request;
	}
	
	public void handleMessage(){
		//TODO: depending on message, different actions should be done.
	}

}
