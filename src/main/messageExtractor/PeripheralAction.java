package messageExtractor;

/**
 * Wrapper for the action extracted from the message sent to the server. This object is returned by the message
 * extractor to be sent to the peripheral specified by the ID.
 * @see MessageExtractorInterface
 */
public class PeripheralAction {
    private long targetId;
    private String action;

    public PeripheralAction(String action, long targetId){
        this.action = action;
        this.targetId = targetId;
    }

    public String getAction(){
        return this.action;
    }

    public long getTargetId(){
        return this.targetId;
    }
}
