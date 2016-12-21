package oezsoy;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

/**
 * Klasse - Client
 * @author Oezsoy Ahmet
 * @version 08.12.2016
 */
public class Client implements Runnable{
	private Socket s;
	private ObjectOutputStream oos;
	
	/**
	 * Konstruktor
	 * @param ip
	 * @param port
	 */
	public Client(String ip, int port){
		try {
			s = new Socket(ip, port);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		
		try {
			oos = new ObjectOutputStream(s.getOutputStream());
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Thread t = new Thread(this);
		t.start();
	}
	
	/**
	 * Main-Methode
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		if (args.length != 2) {
			System.err.println("Anwendung: java chatClient <host name> <port nummer>");
			System.exit(1);
		}
		Client c = new Client(args[0],Integer.parseInt(args[1]));
		Scanner s = new Scanner(System.in);
		while(true){
			String tmp = s.nextLine();
			c.sendMsg(tmp);
		}
	}
	
	@Override
	public void run() {
		try(ObjectInputStream ois = new ObjectInputStream(s.getInputStream());){
			while(true){
				Object tmp = ois.readObject();
				if(tmp instanceof Message){
					Message msg = (Message)tmp;
					System.out.println(msg.getMsg());
				}
			}
		} catch (IOException | ClassNotFoundException e) {
			e.printStackTrace();
			System.exit(0);
		}
		
	}
	
	private void sendMsg(String tmp) {
		try {
			oos.writeObject(new Message(tmp));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}


}
