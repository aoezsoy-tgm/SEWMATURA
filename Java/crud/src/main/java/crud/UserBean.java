package crud;

import java.util.List;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;

/**
 * bean class for interacting with the web tier
 */
@ManagedBean(name="userBean", eager=true)
@RequestScoped
public class UserBean {
	private String nname;
	private String vname;
	public int age;
	public List<User> users = UserDAO.read();
	public User updateUser;
	public List<User> selectedUsers;

	/**
	 * creates and saves a new user
	 * @return index to navigate back to the index file
	 */
	public String saveUser(){
		UserDAO uDao = new UserDAO();
		Integer uid = uDao.getId();
		User user = new User(uid, vname, nname,  age);
		uDao.save(user);
		return "index";
	}
	
	/**
	 * deletes a list of users
	 * @return index to navigate back to the index file
	 */
	public String deleteUser(){
		UserDAO uDao = new UserDAO();
		for(User u: selectedUsers){
			uDao.delete(u);
		}
		return "index";
	}

	/**
	 * updates a user
	 * if no user is selected or if a attribute is not chanced, it doesnt get changed
	 * @return index to navigate back to the index file
	 */
	public String update(){
		UserDAO uDao = new UserDAO();
		if(updateUser != null){
			if(vname==null || vname.equals("")){
				vname = updateUser.getVname();
			}
			if(nname==null || nname.equals("")){
				nname = updateUser.getNname();
			}
			if(age==0){
				age = updateUser.getAge();
			}
			User user = new User(updateUser.getId(), vname, nname,  age);
			uDao.update(user);
		}
		return "index";
	}
	
	public User getUpdateUser() {
		return updateUser;
	}

	public void setUpdateUser(User updateUser) {
		this.updateUser = updateUser;
	}

	public String getNname() {
		return nname;
	}

	public void setNname(String nname) {
		this.nname = nname;
	}

	public String getVname() {
		return vname;
	}

	public void setVname(String vname) {
		this.vname = vname;
	}

	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public List<User> getUsers() {
		return users;
	}
	public void setUsers(List<User> users) {
		this.users = users;
	}
	
	public List<User> getSelectedUsers() {
		return selectedUsers;
	}

	public void setSelectedUsers(List<User> selectedUsers) {
		this.selectedUsers = selectedUsers;
	}
}