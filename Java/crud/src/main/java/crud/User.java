package crud;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 * user class which gets saved in the db
 */
@Entity
@Table(name="user")
public class User {
	@Id
	@Column(name="id")
		private Integer id;
	@Column (name="vname")
	private String vname;
	@Column (name="nname")
		private String nname;
	@Column (name="age")
		private Integer age;
	
	public User(Integer id, String vname, String nname, Integer age){
		this.id = id;
		this.vname = vname;
		this.nname = nname;
		this.age = age;
	}
	public User(){
		this.id = 0;
		this.vname = "null";
		this.nname = "null";
		this.age = 0;
	}
	public Integer getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getVname() {
		return vname;
	}
	public void setVname(String vname) {
		this.vname = vname;
	}
	public String getNname() {
		return nname;
	}
	public void setNname(String nname) {
		this.nname = nname;
	}
	public Integer getAge() {
		return age;
	}
	public void setAge(Integer age) {
		this.age = age;
	}
}