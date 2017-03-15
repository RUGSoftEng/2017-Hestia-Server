package messageExtractor;

import java.io.IOException;

import peripheralDatabase.PeripheralDatabase;
import peripherals.ActionNotDefinedException;
import peripherals.IPeripheral;

/**
 * Wrapper for the action extracted from the message sent to the server. This object is returned by the message
 * extractor to be sent to the peripheral specified by the ID.
 * @see MessageExtractorInterface
 */
public class PeripheralRequestManager extends RequestManager{
	private long targetId;
    private String action;
    // private int value;

    public PeripheralRequestManager(String action, long targetId, PeripheralDatabase database){
    	super("action", database);
        this.action = action;
        this.targetId = targetId;
    }

    public String getAction(){
        return this.action;
    }

    public long getTargetId(){
        return this.targetId;
    }
    
    public void handleMessage(){
    	//TODO: define method getPeripheralInteractor(long targetID)
    	// PeripheralInteractor peripheralI = database.getPeripheralInteractor(targetID)
    	//
    	//try {   
            // peripheralI.performActon(action, value)
        //} catch (ActionNotDefinedException | IOException | InterruptedException e) {
          //  e.printStackTrace();
        //}
    }
}
