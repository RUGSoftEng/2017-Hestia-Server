package messageExtractor;

import peripherals.IPeripheral;

public class RequestManager {
	String type;
	
	public RequestManager(){
		this.type = null;
	}
	
	public RequestManager(String type){
		this.type = type;
	}
	
	public String getType(){
		return this.type;
	}
	
	public void setType(String type){
		this.type = type;
	}
	
	public void handleMessage(IPeripheral target){}

}
