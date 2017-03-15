package messageExtractor;

import peripheralDatabase.PeripheralDatabase;

public interface MessageExtractor{
	public RequestManager parseMessage(String input, PeripheralDatabase peripheralDatabase) throws UnexpectedActionException;
}