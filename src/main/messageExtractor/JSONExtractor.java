package messageExtractor;

import org.json.simple.parser.JSONParser;
import org.json.simple.JSONObject;
import org.json.simple.parser.ParseException;

public class JSONExtractor implements MessageExtractorInterface{
    @Override
    public PeripheralAction handleMessage(String input) throws UnexpectedActionException {
        JSONParser parser = new JSONParser();
        String action = "";
        long id = -1;
        try {
            // Convert input string to JSON object, look for action description
            Object inObj = parser.parse(input);
            JSONObject message = (JSONObject) inObj;
            JSONObject actionDescription = (JSONObject) message.get("action");

            // Parse action type and peripheral id
            action = (String) actionDescription.get("type");
            id = (long) actionDescription.get("id");
        }catch(ParseException | NullPointerException e){
            // If the message we received cannot be parsed or does not contain the required fields, we return
            // no-operation. The clientHandlerThread will take special action upon encountering this object.
            throw new UnexpectedActionException("Unable to parse action",input);
        }
        // Return a new messageObject containing an id and an actionString
        return new PeripheralAction(action,id);
    }

}