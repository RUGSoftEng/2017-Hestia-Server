package MessageExtractor;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class JSONHandlerTest{
    JSONExtractor jsonEx;
    String testMessageOpen;
    String testMessageClose;

    @BeforeEach
    void setUp() {
        jsonEx = new JSONExtractor();
        testMessageOpen = "{\"action\": {\"id\": 1, \"type\": \"openLock\"}}";
        // testMessage is the example message on the message board in Basecamp.
        testMessageClose = "{\"action\": {\"id\": 2, \"type\": \"closeLock\"}}";
    }

    @Test
    void testMessageHandlerOpenLock() {
        try {
            assertEquals("openLock",jsonEx.handleMessage(testMessageOpen).getAction());
        } catch (UnexpectedActionException e) {
            e.printStackTrace();
        }
    }

    @Test
    void setTestMessageCloseLock(){
        try {
            assertEquals("closeLock",jsonEx.handleMessage(testMessageClose).getAction());
        } catch (UnexpectedActionException e) {
            e.printStackTrace();
        }
    }

    @Test
    void testPeripheralID() {
        try {
            assertEquals(1,jsonEx.handleMessage(testMessageOpen).getTargetId());
            assertEquals(2,jsonEx.handleMessage(testMessageClose).getTargetId());
        } catch (UnexpectedActionException e) {
            e.printStackTrace();
        }
    }

    @Test
    void testUndefinedAction() {
        assertThrows(UnexpectedActionException.class, ()->jsonEx.handleMessage("Some garbage String").getAction());
        assertThrows(UnexpectedActionException.class,()->jsonEx.handleMessage("{\"status\": {\"id\": 1}}").getAction
                ());
    }
}