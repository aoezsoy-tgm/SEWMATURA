package oezsoy;

import java.io.ObjectOutputStream;
import java.net.Socket;

/**
 * Klasse - RemoteClient
 * @author Oezsoy Ahmet
 * @version 08.12.2016
 */
public class RemoteClient {
	private Socket s;
	private ObjectOutputStream oos;
	public RemoteClient(Socket s,ObjectOutputStream oos){
		this.s=s;
		this.oos=oos;
	}
	public Socket getS() {
		return s;
	}
	public ObjectOutputStream getOos() {
		return oos;
	}
	
}
