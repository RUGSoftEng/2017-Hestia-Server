package clientInteractors;


/**
 * Created by sebastian on 3/3/17.
 */
public class TCPClientInteractorTest extends ClientInteractorTest {

    @Override
    public void InitWithConcreteImplementation() {
        interactor = new TCPClientInteractor();
    }
}