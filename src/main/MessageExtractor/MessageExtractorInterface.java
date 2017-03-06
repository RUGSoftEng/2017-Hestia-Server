package MessageExtractor;

public interface MessageExtractorInterface{
    public PeripheralAction handleMessage(String input) throws UnexpectedActionException;
}