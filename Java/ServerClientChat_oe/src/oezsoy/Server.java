package oezsoy;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Klasse - Server
 * Ein Chat Server, dass öffentliche und private Nachrichten liefert.
 * @author Oezsoy Ahmet
 * @version 08.12.2016
 */
public class Server implements Runnable {
	/* Server Socket */
	private static ServerSocket serverSocket = null;
	List<RemoteClient> list;

	public Server(int portNumber){
		list =Collections.synchronizedList(new ArrayList<RemoteClient>());
		try {
			serverSocket = new ServerSocket(portNumber);
		} catch (IOException e) {
			System.out.println(e);
		}
		Thread t = new Thread(this);
		t.start();
	}
	/**
	 * Main-Methode
	 * @param args
	 */
	public static void main(String args[]) {
		if (args.length != 1) {
			System.err.println("Anwendung: java Chat <port nummer>");
			System.exit(1);
		}
		new Server(Integer.parseInt(args[0]));
	}
	
	public void sendMsg(Message msg) {
		for(RemoteClient s:list){
			try{
				s.getOos().writeObject(msg);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
	}
	
	public void register(ServerThread t){
		Socket s = t.getClientSocket();
		RemoteClient rc = null;
		try {
			rc = new RemoteClient(s, new ObjectOutputStream(s.getOutputStream()));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		list.add(rc);
		t.start();
	}
	
	@Override
	/**
	 * Erstellt ein Client Socket für jede Verbindung und tut es in einem Client Thread weitergeben.
	 */
	public void run() {
		while (true) {
			try {
				Socket tmp = serverSocket.accept();
				register(new ServerThread(tmp,this));
			} catch (IOException e) {
				System.out.println(e);
			}
		}

	}
}
