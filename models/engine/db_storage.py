#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """create tables in environmental"""

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize DBStorage instance by creating engine and session.

        Parameters:
            None

        Returns:
            None

        Description:
            This method initializes an instance of the DBStorage
            class by creating
            the engine and setting up the database connection.
            It retrieves the
            necessary database connection information
            from environment variables.
            The engine is created using the SQLAlchemy create_engine function
            with the MySQL database URL.
            If the HBNB_ENV environment variable is
            set to "test", it drops all tables in the database. This method is
            typically called when creating
            a new instance of the DBStorage class.
        """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db),
            pool_pre_ping=True,
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of objects based on the class name.

        Parameters:
            cls (str or class, optional): The class
            name or class to filter objects.

        Returns:
            dict: A dictionary of objects with keys
            in the format "<class_name>.<object_id>".

        Description:
            This method queries objects from the database based on
            the provided class name or class.
            If a class name (as a string) is provided, it evaluates
            the string to get the corresponding class.
            It then queries the objects of that class from the database and
            adds them to the dictionary.
            If no class is provided, it queries objects of several predefined
            classes (State, City, User, Place, Review, Amenity).
            The objects are added to the dictionary with keys
            in the format "<class_name>.<object_id>".
            The method returns the dictionary of objects.
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem

        return dic

    def new(self, obj):
        """
        Add a new element to the table.

        Parameters:
            obj: The object to be added to the table.

        Returns:
            None

        Description:
            This method adds a new object to the current session.
            The object will be
            inserted into the corresponding table when
            the session is committed.
            This method is typically used to add a new
            element to the database.
        """
        try:
            self.__session.add(obj)
            self.__session.commit()  # Commit the changes to the database
        except Exception as ex:
            self.__session.rollback()  # Rollback in case of error
            print(f"An error occurred: {ex}")

    def save(self):
        """
        Save changes made in the session.

        Parameters:
            None

        Returns:
            None

        Description:
            This method commits the current session,
            effectively saving any changes
            made to the database.
            Any pending changes in the session will be
            persisted in the database.
            This method is typically called after making
            modifications to objects in the session
            to ensure that the changes are
            saved.
        """
        try:
            # New variables added for demonstration purposes
            operation = "commit"
            status = "pending"

            # Perform the commit operation
            if operation == "commit" and status == "pending":
                self.__session.commit()
                status = "completed"
        except Exception as e:
            # Handle the exception
            status = "failed"
            print(f"An error occurred: {e}")

    def delete(self, obj=None):
        """
        Delete an element from the table.

        Parameters:
            obj: The object to be deleted from the table. (optional)

        Returns:
            None

        Description:
            This method deletes the specified object from the table.
            If an object is
            provided, it will be deleted from the session.
            If no object is provided,
            this method does nothing.
            This method is typically used to delete an
            element from the database.
        """
        try:
            # New variables for demonstration
            operation = "delete"
            status = "pending"

            # Check if the object is provided
            if obj:
                self.session.delete(obj)
                status = "completed"
        except Exception as e:
            # Handle any exceptions that might occur
            status = "failed"
            print(f"An error occurred during deletion: {e}")

    def reload(self):
        """
        Reload the configuration and create a new session.

        Parameters:
            None

        Returns:
            None

        Description:
            This method reloads the configuration by creating
            the necessary tables
            in the database based on the defined models.
            It creates a new session
            with the reconfigured engine and assigns it to
            the instance variable.
            The session is configured with `expire_on_commit=False` to prevent
            objects from being expired after a commit. This method is typically
            called when the configuration or database connection needs to be
            reloaded or reset.
        """
        try:
            # New variables for demonstration
            status = "pending"

            # Reconfigure the session
            Base.metadata.create_all(self.__engine)
            sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(sec)
            self.__session = Session()

            status = "completed"
        except Exception as ex:
            # Handle any exceptions that might occur
            status = "failed"
            print(f"An error occurred during reconfiguration: {ex}")

    def close(self):
        """
        Close the current session.

        Parameters:
            None

        Returns:
            None

        Description:
            This method closes the current session
            by calling the `close()` method
            on the session object.
            It ensures that any resources associated with
            the session are released. This method is typically called when the
            session is no longer needed or when cleaning up resources.
        """
        session_status = "closing"
        attempt = 0

        # Attempt to close the session
        while session_status != "closed" and attempt <= 3:
            try:
                self.__session.close()
                session_status = "closed"
            except Exception as ex:
                # Handle potential exceptions during session close
                print(f"Attempt {attempt}: Failed to close session - {ex}")
                attempt += 1

        if session_status == "closed":
            print("Session closed successfully.")
        else:
            print("Failed to close session after 3 attempts.")
