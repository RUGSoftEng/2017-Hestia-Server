package messageExtractor;

import java.io.IOException;

import peripherals.ActionNotDefinedException;
import peripherals.IPeripheral;

/**
 * Wrapper for the action extracted from the message sent to the server. This object is returned by the message
 * extractor to be sent to the peripheral specified by the ID.
 * @see MessageExtractorInterface
 */
public class PeripheralRequest extends RequestManager{
	private long targetId;
    private String action;

    public PeripheralRequest(String action, long targetId){
    	super("action");
        this.action = action;
        this.targetId = targetId;
    }

    public String getAction(){
        return this.action;
    }

    public long getTargetId(){
        return this.targetId;
    }
    
    public void handleMessage(IPeripheral target){
    	try {   
            target.performAction(action);
        } catch (ActionNotDefinedException | IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
