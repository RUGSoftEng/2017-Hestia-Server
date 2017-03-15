package messageExtractor;

public interface MessageExtractor{
    public PeripheralRequest parseMessage(String input) throws UnexpectedActionException;
}