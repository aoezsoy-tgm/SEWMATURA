package crud;

import org.hibernate.SessionFactory;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.cfg.Configuration;

/**
 * creates a connection to the db
 */
public class HibernateConnection {
	private static SessionFactory sessionFactory;
	static{
		Configuration config = new Configuration().configure("hibernate.cfg.xml");
		StandardServiceRegistryBuilder builder = new StandardServiceRegistryBuilder()
				.applySettings(config.getProperties());
		sessionFactory = config.buildSessionFactory(builder.build());
	}
	/**
	 * provides the connection to other classes
	 * @return sessionFactory
	 */
	public static SessionFactory getSessionFactory(){
		return sessionFactory;
	}
}
