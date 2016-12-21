package Kanyildiz;

import java.io.*;
import java.net.*;

/**
 * 
 * @author Kanyildiz
 * @Datum 14.12.2016
 * @Name Client.java
 *  
**/

public class Client {
	/**
	 * n seiner main()-Methode nutzt der Client die Klasse java.net.Socket zur Einrichtung einer Socket-Verbindung über Port 1010 zu localhost.
	 * Deren Methoden getInputStream() und getOutputStream() liefern Input-, bzw. OutputStreams, aus denen gelesen, bzw. in die geschrieben werden kann.
	 * Zum Schreiben von Strings bietet sich ein PrintStream an, dessen Konstruktor das InputStream-Objekt und einen boolschen Wert für das Autoflushing entgegennimmt.
	 * Seine Methode println() schreibt den gewünschten String und fügt automatisch einen Zeilenumbruch an.
	 * Das Lesen erfolgt zur Performance-Optimierung zunächst in einen BufferedReader, der ein Objekt eines InputStreamReaders im Konstrukor entgegennimmt. Sein Inhalt wird schließlich über eine Schleife Zeile für Zeile ausgelesen und auf die Konsole ausgegeben. Die Methode available() erlaubt bei Bedarf die Abfrage der im InputStream verfügbaren Bytes.
	 * Probleme bei den Input-Output-Vorgängen, sowie ein falscher Host-Name können Exceptions werfen, die in einem try-catch-Block abgefangen werden müssen.
	 * @param args
	 */
	public static void main(String[] args)
	{
		try {
			Socket sock = new Socket("localhost",1010);
			SendThread sendThread = new SendThread(sock);
			Thread thread = new Thread(sendThread);thread.start();
			RecieveThread recieveThread = new RecieveThread(sock);
			Thread thread2 =new Thread(recieveThread);thread2.start();
		} catch (Exception e) {System.out.println(e.getMessage());} 
	}
}
class RecieveThread implements Runnable
{
	Socket sock=null;
	BufferedReader recieve=null;
	
	public RecieveThread(Socket sock) {
		this.sock = sock;
	}//end constructor
	public void run() {
		try{
		recieve = new BufferedReader(new InputStreamReader(this.sock.getInputStream()));//get inputstream
		String msgRecieved = null;
		while((msgRecieved = recieve.readLine())!= null)
		{
			System.out.println("From Server: " + msgRecieved);
			System.out.println("Please enter something to send to server..");
		}
		}catch(Exception e){System.out.println(e.getMessage());}
	}//end run
}//end class recievethread

class SendThread implements Runnable
{
	Socket sock=null;
	PrintWriter print=null;
	BufferedReader brinput=null;
	
	public SendThread(Socket sock)
	{
		this.sock = sock;
	}//end constructor
	
	public void run(){
		try{
		if(sock.isConnected())
		{
			System.out.println("Client connected to "+sock.getInetAddress() + " on port "+sock.getPort());
			this.print = new PrintWriter(sock.getOutputStream(), true);	
		while(true){
			System.out.println("Type your message to send to server..type 'EXIT' to exit");
			brinput = new BufferedReader(new InputStreamReader(System.in));
			String msgtoServerString=null;
			msgtoServerString = brinput.readLine();
			this.print.println(msgtoServerString);
			this.print.flush();
		
			if(msgtoServerString.equals("EXIT"))
			break;
			}//end while
		sock.close();}}catch(Exception e){System.out.println(e.getMessage());}
	}//end run method
}//end class