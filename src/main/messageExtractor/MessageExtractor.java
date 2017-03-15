package messageExtractor;

public interface MessageExtractor{
    public PeripheralAction parseMessage(String input) throws UnexpectedActionException;
}