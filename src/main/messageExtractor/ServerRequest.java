package messageExtractor;

import peripherals.IPeripheral;

public class ServerRequest extends RequestManager{
	private String request;
	
	public ServerRequest(String request){
		super("request");
		this.request = request;
	}
	
	public void handleMessage(IPeripheral target){
		//TODO: depending on message, different actions should be done.
	}

}
