package clientHandler;

import org.junit.After;
import org.junit.Before;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.*;

class ClientHandlerThreadTest {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private String testMessage;

    @Before
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @BeforeEach
    void setUp(){
        testMessage = "{\"action\": {\"id\": 1, \"type\": \"openLock\"}}";
    }

    @Test
    void testMessageParsing(){
        String expectedResponseMessage =  "127.0.0.1:8800\n" + "openLock";
        new Thread(new ClientHandlerThread(testMessage)).start();
        //TODO test case incomplete, need a way to check if the message is being constructed correctly in the thread
        //assertEquals(expectedResponseMessage,outContent.toString());
    }

    @After
    public void cleanUpStreams() {
        System.setOut(null);
    }

}