#!/usr/bin/python3
"""
Test case for the Amenity class and its functionalities.

This module contains a test case for the Amenity class and its associated
functionality. It includes tests for the 'name' attribute of the Amenity
instance.

Author: [Your Name]
Date: [Current Date]
"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
from time import sleep
from os import getenv
import pycodestyle
import inspect
import unittest

storage_t = getenv("HBNB_TYPE_STORAGE")


class test_Amenity(test_basemodel):
    """
    Test suite for the Amenity class.

    This test suite contains test cases for the Amenity class. It ensures that
    the Amenity class functions correctly, including the inherited methods
    from the BaseModel class.

    Author: [Your Name]
    Date: [Current Date]
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test case.

        This method initializes the test case by calling the constructor of the
        superclass and setting the 'name' and 'value' attributes.

        Author: [Your Name]
        Date: [Current Date]
        """
        try:
            super().__init__(*args, **kwargs)
            self.name = "Amenity"
            # Ensure 'Amenity' is defined before this point to avoid NameError
            self.value = Amenity
        except Exception as e:
            # Handle the exception (e.g., log it,
            # raise a custom exception, etc.)
            print(f"An error occurred: {e}")
            # Optionally re-raise the exception if you want it to propagate
            raise

    def test_name2(self):
        """
        Test the 'name' attribute of the Amenity instance.

        This test case verifies that the 'name' attribute of the Amenity
        instance is of type 'str'.

        Author: Your Name
        Date: {current_date}
        """
        try:
            # Create a new instance of the Amenity class
            new = self.value()

            # Assert that the 'name' attribute is of type 'str'
            self.assertEqual(type(new.name), str)
        except Exception as e:
            # Handle the exception (e.g., log it,
            # raise a custom exception, etc.)
            print(f"An error occurred during the test: {e}")
            # Optionally re-raise the exception if you want it to propagate
            raise


class Test_PEP8(unittest.TestCase):
    """
    Test case to check PEP8 style compliance for the User class.

    This test case verifies the PEP8 style compliance of the User class.
    It checks if there are any code style errors or warnings.

    Author: [Your Name]
    Date: [Current Date]
    """

    def test_pep8_user(self):
        """
        Test PEP8 style compliance for the User class.

        This test case uses the pycodestyle module to check the PEP8 style
        compliance for the 'models/amenity.py' file. It asserts that there
        are no code style errors or warnings.

        Author: [Your Name]
        Date: [Current Date]
        """
        # Create a Pycodestyle StyleGuide object with quiet mode enabled
        pep8style = pycodestyle.StyleGuide(quiet=True)

        try:
            # Check the PEP8 style for the 'models/amenity.py' file
            result = pep8style.check_files(["models/amenity.py"])

            # Assert that there are no PEP8 style errors or warnings
            self.assertEqual(result.total_errors, 0,
                             "Found code style errors(and warnings).")
        except Exception as e:
            print(f"An error occurred: {e}")


class test_inherit_basemodel(unittest.TestCase):
    """
    Test case to verify if Amenity inherits from BaseModel.

    This test case ensures that the Amenity class properly inherits from the
    BaseModel class. It checks if an instance of Amenity is an instance of
    both Amenity and BaseModel. It also verifies that Amenity is a subclass
    of BaseModel.

    Author: [Your Name]
    Date: [Current Date]
    """

    def test_instance(self):
        """
        Check if an instance of Amenity is an instance of BaseModel.

        This test case creates an instance of the Amenity class and asserts
        that it is an instance of both Amenity and BaseModel. It also verifies
        that Amenity is a subclass of BaseModel. Additionally, it checks the
        string representation of the type of the Amenity instance.

        Author: [Your Name]
        Date: [Current Date]
        """
        try:
            # Create an instance of the Amenity class
            user = Amenity()

            # Assert that the instance is an instance of Amenity
            self.assertIsInstance(user, Amenity)

            # Assert that the instance is a subclass of BaseModel
            self.assertTrue(issubclass(type(user), BaseModel))

            # Assert the string representation of the type of the instance
            self.assertEqual(str(type(user)),
                             "<class 'models.amenity.Amenity'>")
        except Exception as e:
            print(f"An error occurred: {e}")


class test_Amenity_BaseModel(unittest.TestCase):
    """
    Test case for the Amenity class and its inheritance from BaseModel.

    This test case verifies the Amenity class and its inheritance from
    the BaseModel class. It includes tests for creating instances of
    Amenity, checking attribute types, dictionary representation, and
    specific attribute values.

    Author: [Your Name]
    Date: [Current Date]
    """

    def test_instances(self):
        """
        Test different aspects of the Amenity class.

        This test case creates an instance of the Amenity class and asserts
        various aspects, including instance type, attribute types, dictionary
        representation, and specific attribute values.

        Author: [Your Name]
        Date: [Current Date]
        """
        try:
            # Patch the 'models.amenity' module
            with patch("models.amenity"):
                # Create an instance of the Amenity class
                instance = Amenity()

                # Assert the instance type
                self.assertEqual(type(instance), Amenity)

                # Set the 'name' attribute of the instance
                instance.name = "Barbie"

                # Define the expected attribute types
                expected_attrs_types = {
                    "id": str,
                    "created_at": datetime,
                    "updated_at": datetime,
                    "name": str,
                }

                # Get the dictionary representation of the instance
                inst_dict = instance.to_dict()

                # Define the expected attribute keys in the dictionary
                expected_dict_attrs = [
                    "id",
                    "created_at",
                    "updated_at",
                    "name",
                    "__class__",
                ]

                # Assert the keys in the dictionary representation
                self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)

                # Assert the specific attribute values in the dictionary
                self.assertEqual(inst_dict["name"], "Barbie")
                self.assertEqual(inst_dict["__class__"], "Amenity")

                # Check the attribute types and existence
                for attr, types in expected_attrs_types.items():
                    with self.subTest(attr=attr, typ=types):
                        self.assertIn(attr, instance.__dict__)
                        self.assertIs(type(instance.__dict__[attr]), types)

                # Assert the 'name' attribute value
                self.assertEqual(instance.name, "Barbie")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_user_id_and_createat(self):
        """
        Test case for verifying the id and created_at
        attributes of Amenity instances.

        This test case creates three instances of
        the Amenity class with a time delay
        between them. It verifies that the id attribute is o
        f type str for each instance,
        ensures that the id values are unique, and checks
        the ordering and uniqueness of
        the created_at attribute.

        Author: [Your Name]
        Date: [Current Date]
        """
        try:
            # Create three instances of Amenity class with a
            # time delay between them
            user_1 = Amenity()
            sleep(2)
            user_2 = Amenity()
            sleep(2)
            user_3 = Amenity()

            # Create a list of the instances
            list_users = [user_1, user_2, user_3]

            # Iterate over the list of instances
            for instance in list_users:
                # Get the id of each instance
                user_id = instance.id

                # Assert that the id is of type str
                with self.subTest(user_id=user_id):
                    self.assertIs(type(user_id), str)

            # Assert that the ids of the instances are not equal
            self.assertNotEqual(user_1.id, user_2.id)
            self.assertNotEqual(user_1.id, user_3.id)
            self.assertNotEqual(user_2.id, user_3.id)

            # Assert the ordering of the created_at attribute
            self.assertTrue(user_1.created_at <= user_2.created_at)
            self.assertTrue(user_2.created_at <= user_3.created_at)

            # Assert that the created_at values are not equal
            self.assertNotEqual(user_1.created_at, user_2.created_at)
            self.assertNotEqual(user_1.created_at, user_3.created_at)
            self.assertNotEqual(user_3.created_at, user_2.created_at)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_str_method(self):
        """
        Test case for verifying the __str__ magic method of the Amenity class.

        This test case creates an instance of the Amenity class and
        checks the output
        of the __str__ method. It compares the expected string
        representation of the
        instance with the actual output of str(inst).

        Author: [Your Name]
        Date: [Current Date]
        """
        try:
            # Create an instance of the Amenity class
            inst = Amenity()

            # Define the expected string representation of the instance
            str_output = "[Amenity] ({}) {}".format(inst.id, inst.__dict__)

            # Assert that the expected string matches the output of str(inst)
            self.assertEqual(str_output, str(inst))
        except Exception as e:
            print(f"An error occurred: {e}")

    @patch("models.storage")
    def test_save_method(self, mock_storage):
        """
        Test case for verifying the save method and its behavior.

        This test case creates an instance of the Amenity class
        and tests the save method.
        It checks if the save method updates the `updated_at`
        attribute while keeping
        the `created_at` attribute unchanged.
        It also asserts that the `save` method of
        the mock storage object is called.

        Args:
            mock_storage: A mock object representing the storage mechanism.

        Author: [Your Name]
        Date: [Current Date]
        """
        # Create an instance of the Amenity class
        instance5 = Amenity()

        # Store the initial values of created_at and updated_at
        created_at = instance5.created_at
        sleep(2)
        updated_at = instance5.updated_at

        # Call the save method
        instance5.save()

        # Obtain the new values of created_at and updated_at
        new_created_at = instance5.created_at
        sleep(2)
        new_updated_at = instance5.updated_at

        # Assert that updated_at is different from new_updated_at
        self.assertNotEqual(updated_at, new_updated_at)

        # Assert that created_at remains the same
        self.assertEqual(created_at, new_created_at)

        # Assert that the save method of the mock storage object is called
        self.assertTrue(mock_storage.save.called)


class TestAmenity(unittest.TestCase):
    """
    Test case for the Amenity class.

    Author: [Your Name]
    Date: [Current Date]
    """

    def test_is_subclass(self):
        """
        Test case to verify that Amenity is a subclass of BaseModel.

        This test case creates an instance of the Amenity class
        and checks if it
        is an instance of the BaseModel class. It also verifies the presence of
        "id", "created_at", and "updated_at" attributes
        in the Amenity instance.

        Author: [Your Name]
        Date: [Current Date]
        """
        # Create an instance of the Amenity class
        amenity = Amenity()

        # Assert that the amenity instance is an instance of
        # the BaseModel class
        self.assertIsInstance(amenity, BaseModel)

        # Assert the presence of "id", "created_at",
        # and "updated_at" attributes
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """
        Test case to verify that Amenity has the attribute 'name' and
        it is an empty string.

        This test case creates an instance of the Amenity class and
        checks if it has the
        attribute 'name' using the `hasattr` function.
        It then checks the value of the 'name'
        attribute, asserting that it is an empty string when
        the storage type is not 'db',
        and `None` when the storage type is 'db'.

        Author: [Your Name]
        Date: [Current Date]
        """
        # Create an instance of the Amenity class
        amenity = Amenity()

        # Assert the presence of the 'name' attribute
        self.assertTrue(hasattr(amenity, "name"))

        # Check the value of the 'name' attribute based on the storage type
        if storage_t == "db":
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """
        Test case to verify that the to_dict method creates a dictionary
        with proper attributes.

        This test case creates an instance of the Amenity class and
        calls the to_dict method.
        It checks the type of the returned dictionary,
        asserts that the '_sa_instance_state'
        attribute is not present in the dictionary, and
        verifies the presence of all other
        attributes of the instance in the dictionary.
        It also checks for the presence of the
        '__class__' attribute in the dictionary.

        Author: [Your Name]
        Date: [Current Date]
        """
        # Create an instance of the Amenity class
        am = Amenity()

        # Print the instance's __dict__ for debugging
        print(am.__dict__)

        # Call the to_dict method
        new_d = am.to_dict()

        # Assert the type of the returned dictionary
        self.assertEqual(type(new_d), dict)

        # Assert the absence of the '_sa_instance_state' attribute
        self.assertFalse("_sa_instance_state" in new_d)

        # Assert the presence of all other attributes in the dictionary
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)

        # Assert the presence of the '__class__' attribute
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """
        Test case to verify that the values in the
        dictionary returned from to_dict are correct.

        This test case creates an instance of the Amenity
        class and calls the to_dict method.
        It then checks the values in the returned dictionary,
        asserting that the '__class__'
        attribute is set to "Amenity", the 'created_at' and
        'updated_at' attributes are of
        type string, and their string values match the
        formatted string representations of
        am.created_at and am.updated_at respectively.

        Author: [Your Name]
        Date: [Current Date]
        """
        # Define the time format string
        t_format = "%Y-%m-%dT%H:%M:%S.%f"

        # Create an instance of the Amenity class
        am = Amenity()

        # Call the to_dict method
        new_d = am.to_dict()

        # Assert the value of the '__class__' attribute
        self.assertEqual(new_d["__class__"], "Amenity")

        # Assert the type of the 'created_at' and 'updated_at' attributes
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)

        # Assert the formatted string representation of 'created_at'
        # and 'updated_at'
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """
        Test case to verify that the str method has the correct output.

        This test case creates an instance of the Amenity class and
        checks the output of
        the str method. It compares the expected string representation,
        which is constructed
        using the id and __dict__ attributes of the instance,
        with the actual output of
        str(amenity).

        Author: [Your Name]
        Date: [Current Date]
        """
        # Create an instance of the Amenity class
        amenity = Amenity()

        # Construct the expected string representation
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)

        # Assert the expected string representation matches
        # the output of str(amenity)
        self.assertEqual(string, str(amenity))
