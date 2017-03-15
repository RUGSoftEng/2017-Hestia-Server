package messageExtractor;

import org.json.simple.parser.JSONParser;
import org.json.simple.JSONObject;
import org.json.simple.parser.ParseException;

import peripheralDatabase.PeripheralDatabase;

/**
 * This class parses a JSON message. It will create a message object to be used
 * by the ClientHandler.
 * @see MessageExtractor
 * @see ClientHandler
 */
public class MessageJSONParser implements MessageExtractor{
    @Override
    public RequestManager parseMessage(String input, PeripheralDatabase peripheralDatabase) throws UnexpectedActionException {
    	JSONParser parser = new JSONParser();
    	RequestManager messageToHandle = new RequestManager(peripheralDatabase);
        try {
            // Convert input string to JSON object, look for action description
            Object inObj = parser.parse(input);
            JSONObject jsonOb = (JSONObject) inObj;
            String typeOfMessage = (String) jsonOb.get("type");

            if(typeOfMessage.equals("action")){
                // Parse action type and peripheral id
            	String action = "";
                long id = -1;
            	JSONObject message = (JSONObject) jsonOb.get("message");
                action = (String) message.get("action");
                id = (long) message.get("id");
                
                messageToHandle = new PeripheralRequestManager(action,id, peripheralDatabase);
            }
            
            if(typeOfMessage.equals("request")){
            	String message = (String) jsonOb.get("message");
            	messageToHandle =  new ServerRequestManager(message, peripheralDatabase);
            }
        }catch(ParseException | NullPointerException e){
            // If the message we received cannot be parsed or does not contain the required fields, we return
            // no-operation. The clientHandlerThread will take special action upon encountering this object.
            throw new UnexpectedActionException("Unable to parse action",input);
        }
        // Return a new messageObject containing an id and an actionString
		return messageToHandle;
        
    }


}