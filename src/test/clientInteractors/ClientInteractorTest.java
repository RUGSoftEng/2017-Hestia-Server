package clientInteractors;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by sebastian on 3/3/17.
 */
public abstract class ClientInteractorTest {
    ClientInteractorInterface interactor;

    @Before
    public abstract void InitWithConcreteImplementation();

    @Test
    public void isNotConnected() throws Exception {
        assertEquals(true, interactor.isNotConnected());
    }

}