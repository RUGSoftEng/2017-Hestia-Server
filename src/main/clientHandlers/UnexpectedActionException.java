package clientHandlers;

public class UnexpectedActionException extends Exception{
    public UnexpectedActionException(){
        super("Received an unexpected action message");
    }

    UnexpectedActionException(String message, String offender){
        super(message);
        System.err.println("Unable to parse the following message, which should contain an action definition: " +
                offender);
    }
}
