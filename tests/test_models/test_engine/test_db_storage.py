#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""
from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pycodestyle
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorageDocs(unittest.TestCase):
    """Test case for checking the documentation and style of DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up class for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """
        Test that models/engine/db_storage.py
        conforms to PEP8 style guide
        """
        try:
            pep8s = pycodestyle.StyleGuide(quiet=True)
            result = pep8s.check_files(['models/engine/db_storage.py'])
            self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings)."
            )
        except Exception as e:
            self.fail(f"An exception occurred: {str(e)}")

    def test_pep8_conformance_test_db_storage(self):
        """
        Test that tests/test_models/test_db_storage.py
        conforms to PEP8 style guide
        """
        try:
            pep8s = pycodestyle.StyleGuide(quiet=True)
            result = pep8s.check_files
            (['tests/test_models/test_engine/test_db_storage.py'])
            self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings)."
            )
        except Exception as e:
            self.fail(f"An exception occurred: {str(e)}")

    def test_db_storage_module_docstring(self):
        """
        Test for the presence and length
        of db_storage.py module docstring
        """
        try:
            self.assertIsNotNone(
                db_storage.__doc__,
                "db_storage.py needs a docstring"
            )
            self.assertTrue(
                len(db_storage.__doc__) >= 1,
                "db_storage.py needs a docstring"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {str(e)}")

    def test_db_storage_class_docstring(self):
        """Test for the presence and length of DBStorage class docstring"""
        try:
            self.assertIsNotNone(
                DBStorage.__doc__,
                "DBStorage class needs a docstring"
            )
            self.assertTrue(
                len(DBStorage.__doc__) >= 1,
                "DBStorage class needs a docstring"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {str(e)}")

    def test_dbs_func_docstrings(self):
        """
        Test for the presence and length
        of docstrings in DBStorage methods
        """
        try:
            for func in self.dbs_f:
                self.assertIsNotNone(
                    func[1].__doc__,
                    f"{func[0]} method needs a docstring"
                )
                self.assertTrue(
                    len(func[1].__doc__) >= 1,
                    f"{func[0]} method needs a docstring"
                )
        except Exception as e:
            self.fail(f"An exception occurred: {str(e)}")


class TestFileStorage(unittest.TestCase):
    """Test case for FileStorage class"""

    @unittest.skipIf(
        storage_t != 'db',
        "not testing db storage"
    )
    def test_all_returns_dict(self):
        """Test that the all method returns a dictionary"""
        try:
            self.assertIs(
                type(models.storage.all()),
                dict,
                "models.storage.all() should return a dictionary"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {str(e)}")

    @unittest.skipIf(
        storage_t != 'db',
        "not testing db storage"
    )
    def test_all_no_class(self):
        """Test that all method returns all rows when no class is passed"""
        try:
            # Perform the test here
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {str(e)}")

    @unittest.skipIf(
        storage_t != 'db',
        "not testing db storage"
    )
    def test_new(self):
        """Test that new method adds an object to the database"""
        try:
            # Perform the test here
            pass
        except Exception as e:
            self.fail(f"Anexception occurred: {str(e)}")

    @unittest.skipIf(
        storage_t != 'db',
        "not testing db storage"
    )
    def test_save(self):
        """Test that save method properly saves objects to file.json"""
        try:
            # Perform the test here
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {str(e)}")
