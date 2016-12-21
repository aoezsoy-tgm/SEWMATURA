package oezsoy;

import java.io.Serializable;

/**
 * Klasse - Message
 * @author Oezsoy Ahmet
 * @version 08.12.2016
 */
public class Message implements Serializable{
	private String msg;
	public Message(String msg){
		this.msg=msg;
	}
	public String getMsg() {
		return msg;
	}
	public void setMsg(String msg) {
		this.msg = msg;
	}
	
}
