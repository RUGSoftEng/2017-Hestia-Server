package peripherals;

/**
 * When an action on a peripheral is not defined, this action is thrown.
 */
public class ActionNotDefinedException extends Exception{
    ActionNotDefinedException(){
        System.err.println("This action is not defined for this peripheral");
    }
	
	private static final long serialVersionUID = 1L;

}
