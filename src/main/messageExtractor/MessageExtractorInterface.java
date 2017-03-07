package messageExtractor;

public interface MessageExtractorInterface{
    public PeripheralAction handleMessage(String input) throws UnexpectedActionException;
}