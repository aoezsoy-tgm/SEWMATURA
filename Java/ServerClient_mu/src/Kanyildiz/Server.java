package Kanyildiz;

import java.io.*;
import java.net.*;
import java.lang.*;

/**
 * 
 * @author Kanyildiz
 * @Datum 14.12.2016
 * @Name Server.java
 *  
**/

public class Server {
	/**
	 * Mit dieser Klasse wird ein Server aufgestellt, das auf ein Client wartet.
	 * Wenn der richtige Port sowie IP-Adresse angesprochen wird, wird die Connection aufgebaut
	 * und der Server kann somit mit dem Clienten Chatten.
	 * Dafür werden die Entsprechenden Methoden unten erklärt.
	 * 
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		// Der Port wird definiert, bzw eine Variable erstellt die nicht überschreiben werden kann.
		final int port = 1010;
		System.out.println("Server wartet auf Client... ");
		// Ein Objekt von ServerSocket mit dem Port wird zugewisen.
		ServerSocket ss = new ServerSocket(port);
		// Wenn ein Client kommt wird es erstmal aufgenommen.
		Socket clientSocket = ss.accept();
		System.out.println("Client IP-Adresse: "+clientSocket.getInetAddress()+" ||| Client Port: "+clientSocket.getPort());
		//2 Threads werden hier creiert: 1 zum senden und 1 zum enpfangen. Sie werden entsprechend gestartet.
		ClientThreadM recieve = new ClientThreadM(clientSocket);
		Thread thread = new Thread(recieve);
		thread.start();
		MessageClient send = new MessageClient(clientSocket);
		Thread thread2 = new Thread(send);
		thread2.start();
	}}


class ClientThreadM implements Runnable {
	/**
	 *  Hierzu läuft der Server in einer Endlosschleife: sobald über "serverSocket.accept()" eine
	 *  Verbindung eingeht, wird ein neuer Thread gestartet der die Verarbeitung dieser Verbindung übernimmt. 
	 *  Der Server ist direkt danach für weitere Verbindungen bereit. 
	 *  Es wird ein Client geschrieben, der eine Verbindung zum Server aufbaut und von diesem die Antwort "Serverantwort" erhält 
	 */
	Socket clientSocket=null;
	BufferedReader brBufferedReader = null;
	
	public ClientThreadM(Socket clientSocket)
	{
		this.clientSocket = clientSocket;
	}//end constructor

	public void run() {
		try{
		brBufferedReader = new BufferedReader(new InputStreamReader(this.clientSocket.getInputStream()));		
		
		String messageString;
		while(true){
		while((messageString = brBufferedReader.readLine())!= null){
			//Message vom Clienten
			if(messageString.equals("EXIT"))
			{
				break;
				//break wenn die nachricht EXIT eigegeben wird.
			}
			System.out.println("Client: " + messageString);
			//Die Nachricht vom Clienten ausgeben
			System.out.println("Ihre Message...");
		}
		this.clientSocket.close();
		System.exit(0);
	}
		
	}
	catch(Exception ex){System.out.println(ex.getMessage());}
	}
}

class MessageClient implements Runnable{
	/**
	 * Eingabe-Reader und Ausgabe-Writer erzeugen.
	 * Es wird hier nur mit Text gearbeitet und zeilenweise eingelesen bzw. geschrieben.
	 * In einer Endlosschleife auf Eingaben horchen bis die Verbindung beendet wird
	 * und ein "readLine" dadurch nichts mehr zurückliefert. 
	 * Die Eingabe in "UpperCase" umwandeln und als komplette Zeile an Client zurückschieben.
	 * "println" sorgt dafür, dass die Daten gesendet werden.
	 * 
	 */
	PrintWriter pwPrintWriter;
	Socket clientSock = null;
	
	public MessageClient(Socket clientSock)
	{
		this.clientSock = clientSock;
	}
	public void run() {
		try{
		pwPrintWriter =new PrintWriter(new OutputStreamWriter(this.clientSock.getOutputStream()));//get outputstream
		
		while(true)
		{
			String msgToClientString = null;
			BufferedReader input = new BufferedReader(new InputStreamReader(System.in));//get userinput
			
			msgToClientString = input.readLine();//Message von Client
			
			pwPrintWriter.println(msgToClientString);//send message to client with PrintWriter
			pwPrintWriter.flush();//flush the PrintWriter
			System.out.println("Please enter something to send back to client..");
		}//end while
		}
		catch(Exception ex){System.out.println(ex.getMessage());}	
	}//end run
}