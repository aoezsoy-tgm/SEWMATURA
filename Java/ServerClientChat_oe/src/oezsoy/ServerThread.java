package oezsoy;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.Socket;

/**
 * Klasse - ServerThread
 * @author Oezsoy Ahmet
 * @version 08.12.2016
 */
class ServerThread extends Thread {
	private Socket clientSocket;
	private Server server;
	public ServerThread(Socket clientSocket, Server server) {
		this.clientSocket = clientSocket;
		this.server=server;
	}

	public void run() {
		try(ObjectInputStream ois = new ObjectInputStream(clientSocket.getInputStream())){
			while(true){
				Object tmp = ois.readObject();
				if(tmp instanceof Message){
					Message msg = (Message)tmp;
					server.sendMsg(msg);
				}
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("Garbage Collector!");
	}

	public Socket getClientSocket() {
		return clientSocket;
	}
	
}

