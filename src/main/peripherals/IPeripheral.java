package peripherals;
import java.io.IOException;

/**
 * Interface for all peripherals. For every new peripheral type that is added to the 
 * system this interface needs to be implemented.
 */
public interface IPeripheral {
	/**
	 * This method is called with a string representing the action that should be performed.
	 * @param action = Action that should be performed by the peripheral
	 * @throws ActionNotDefinedException
	 * @throws IOException
	 * @throws InterruptedException
	 */
	public void performAction(String action) throws ActionNotDefinedException, IOException, InterruptedException;
}
