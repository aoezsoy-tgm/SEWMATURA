package crud;

import java.util.List;
import org.hibernate.Criteria;
import org.hibernate.Session;

/**
 * for accessing the db
 */
public class UserDAO {
	Session session = HibernateConnection.getSessionFactory().openSession();
	/**
	 * saves a user into the db (self-explaining)
	 * @param user which shall be saved in the db
	 */
	public void save(User user){
		session.beginTransaction();
		session.save(user);
		session.getTransaction().commit();
		session.close();
	}
	
	/**
	 * determines a new id
	 * @return a new id
	 */
	public Integer getId() {
		String select = "select max(user.id) from User user";
		List<Integer> resultSet = session.createQuery(select).list();
		Integer uID = 1;
		if(resultSet.get(0) != null){
			uID = resultSet.get(0) + 1;
		}
		return uID;
	}
	
	/**
	 * opens a new session and reads users that matches the Critera (obviously every user (User.class))
	 * @return list of (all) users
	 */
	public static List<User> read(){
		Session session = HibernateConnection.getSessionFactory().openSession();
		session.beginTransaction();
		Criteria cr = session.createCriteria(User.class);
		List<User> uList = cr.list();
		session.getTransaction().commit();
		session.close();
		return uList;
	}

	/**
	 * deletes a user
	 * @param u user which gets deleted
	 */
	public void delete(User u) {
		Session session = HibernateConnection.getSessionFactory().openSession();
		session.beginTransaction();
		session.delete(u);
		session.getTransaction().commit();
		session.close();
	}

	/**
	 * updates a user
	 * @param updateUser user which gets updated
	 */
	public void update(User updateUser) {
		Session session = HibernateConnection.getSessionFactory().openSession();
		session.beginTransaction();
		session.saveOrUpdate(updateUser);
		session.getTransaction().commit();
		session.close();
	}	
}