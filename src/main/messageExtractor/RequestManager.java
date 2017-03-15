package messageExtractor;

import peripheralDatabase.PeripheralDatabase;
import peripherals.IPeripheral;

/**
 * This class is the super class of PeripheralRequestManager and ServerRequestManager.
 */
public class RequestManager {
	String type;
	PeripheralDatabase peripheralDatabase;
	
	public RequestManager(PeripheralDatabase database){
		this.type = null;
		this.peripheralDatabase = database;
	}
	
	public RequestManager(String type, PeripheralDatabase database){
		this.type = type;
		this.peripheralDatabase = database;
	}
	
	public String getType(){
		return this.type;
	}
	
	public void setType(String type){
		this.type = type;
	}
	
	public void handleMessage(){}

}
