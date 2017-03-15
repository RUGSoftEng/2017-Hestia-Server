package messageExtractor;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class JSONHandlerTest{
    MessageJSONParser jsonEx;
    String testMessageOpen;
    String testMessageClose;

    @BeforeEach
    void setUp() {
        jsonEx = new MessageJSONParser();
        testMessageOpen = "{\"action\": {\"id\": 1, \"type\": \"openLock\"}}";
        // testMessage is the example message on the message board in Basecamp.
        testMessageClose = "{\"action\": {\"id\": 2, \"type\": \"closeLock\"}}";
    }

    @Test
    void testMessageHandlerOpenLock() {
        try {
            assertEquals("openLock",jsonEx.parseMessage(testMessageOpen).getAction());
        } catch (UnexpectedActionException e) {
            e.printStackTrace();
        }
    }

    @Test
    void setTestMessageCloseLock(){
        try {
            assertEquals("closeLock",jsonEx.parseMessage(testMessageClose).getAction());
        } catch (UnexpectedActionException e) {
            e.printStackTrace();
        }
    }

    @Test
    void testPeripheralID() {
        try {
            assertEquals(1,jsonEx.parseMessage(testMessageOpen).getTargetId());
            assertEquals(2,jsonEx.parseMessage(testMessageClose).getTargetId());
        } catch (UnexpectedActionException e) {
            e.printStackTrace();
        }
    }

    @Test
    void testUndefinedAction() {
        assertThrows(UnexpectedActionException.class, ()->jsonEx.parseMessage("Some garbage String").getAction());
        assertThrows(UnexpectedActionException.class,()->jsonEx.parseMessage("{\"status\": {\"id\": 1}}").getAction
                ());
    }
}