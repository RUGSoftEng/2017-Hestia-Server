package messageHandlers;

import clientHandlers.JSONExtractor;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

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
    void testMessageHandlerLock() {
        assertEquals("openLock",jsonEx.handleMessage(testMessageOpen).getAction());
        assertEquals("closeLock",jsonEx.handleMessage(testMessageClose).getAction());
    }

    @Test
    void testPeripheralID() {
        assertEquals(1,jsonEx.handleMessage(testMessageOpen).getTargetId());
        assertEquals(2,jsonEx.handleMessage(testMessageClose).getTargetId());
    }

    @Test
    void testNOP() {
        assertEquals("NOP",jsonEx.handleMessage("Some garbage String").getAction());
        assertEquals("NOP",jsonEx.handleMessage("{\"status\": {\"id\": 1}}").getAction());
    }
}