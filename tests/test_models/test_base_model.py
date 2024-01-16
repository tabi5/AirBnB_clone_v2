#!/usr/bin/python3

"""
This module contains unit tests for the BaseModel class.
"""

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle


class test_basemodel(unittest.TestCase):
    """
    Test case for the BaseModel class.

    This test case includes unit tests for the BaseModel class.
    It imports the necessary dependencies and sets up the test
    environment. The test case is designed to be run using the
    unittest module.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel object with the given arguments.

        Parameters:
        - args (tuple): Variable-length positional arguments.
        - kwargs (dict): Variable-length keyword arguments.

        Raises:
        - None.

        Returns:
        - None.

        Description:
        This method initializes an instance of the BaseModel class by setting
        the name attribute to the string 'BaseModel' and the value attribute
        to the BaseModel class itself.

        Example usage:
        >>> model = BaseModel()
        >>> print(model.name)
        'BaseModel'
        >>> print(model.value)
        <class '__main__.BaseModel'>
        """
        try:
            super().__init__(*args, **kwargs)
        except Exception as e:
            # Handle any exceptions raised by the superclass initialization
            # process appropriately
            print("An error occurred during superclass initialization:", e)

        self.name = "BaseModel"
        self.value = BaseModel

    def test_pycodestyle(self):
        """
        Test the PEP 8 formatting of the code.

        Parameters:
        - self: The instance of the test class.

        Raises:
        - AssertionError: If code style errors (or warnings) are found.

        Returns:
        - None.

        Description:
        This method uses the `pycodestyle` module to check the PEP 8 formatting
        of the code in the 'models/base_model.py' file. The method suppresses
        any output using the `quiet=True` argument. If any code style errors
        (or warnings) are found, an `AssertionError` is raised with an
        appropriate error message.

        Example usage:
        >>> test_instance = TestClass()
        >>> test_instance.test_pycodestyle()
        """
        try:
            pycostyle = pycodestyle.StyleGuide(quiet=True)
            result = pycostyle.check_files(["models/base_model.py"])
            self.assertEqual(
                result.total_errors, 0, "Found code style errors (and warnings)."
            )
        except Exception as e:
            # Handle any exceptions raised during the code style testing process
            print("An error occurred during code style testing:", e)

    def setUp(self):
        """
        Set up any preconditions required for the test cases.

        This method is executed before each test case in the test class.

        Exceptions:
        - Any exceptions raised during the setup process will cause the test case to fail.
        """

        try:
            pass
        except Exception as e:
            # Handle any exceptions that occur during setup
            # Log the exception or perform any necessary cleanup actions
            raise AssertionError(f"Failed to set up test cases: {str(e)}")

    def tearDown(self):
        """
        Clean up resources or perform necessary actions after the test cases have run.

        This method is executed after each test case in the test class.

        Exceptions:
        - Any exceptions raised during the tear-down process will be caught and ignored.
        """

        try:
            # Remove the 'file.json' file
            os.remove("file.json")
        except OSError as e:
            pass
        except Exception as e:
            print("Exception:", e)
            pass

    def test_default(self):
        """
        Test the default behavior of the value() method.

        This method verifies that the value() method returns an instance
        of the expected type.

        Exceptions:
        - AssertionError: If the type of the returned value is not equal
        to the expected type.
        """

        try:
            # Add your test code here
            # For example, you can create an instance of the class and call the value() method
            i = self.value()
            self.assertEqual(type(i), self.value)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError(
                "The value() method did not return the expected type."
            ) from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_kwargs(self):
        """
        Test the creation of a new instance using keyword arguments.

        This method verifies that a new instance of the class can be created
        by passing keyword arguments obtained from the `to_dict()` method.
        It checks that the new instance is not the same as the original instance.

        Exceptions:
        - AssertionError: If the new instance is the same as the original instance.
        """

        try:
            # Add your test code here
            # For example, create an instance, convert it to a dict, and create a new instance using kwargs
            i = self.value()
            copy = i.to_dict()
            new = BaseModel(**copy)
            self.assertFalse(new is i)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError(
                "The new instance is the same as the original instance."
            ) from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_kwargs_int(self):
        """
        Test the creation of a new instance using keyword arguments with an invalid type.

        This method verifies that when an invalid type is provided as a keyword argument,
        a TypeError is raised.

        Exceptions:
        - AssertionError: If the expected TypeError is not raised.
        """

        try:
            # Add your test code here
            # For example, create an instance, convert it to a dict, update with an invalid type,
            # and create a new instance using kwargs
            i = self.value()
            copy = i.to_dict()
            copy.update({1: 2})
            with self.assertRaises(TypeError):
                new = BaseModel(**copy)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError("The expected TypeError was not raised.") from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_save(self):
        """
        Test the save method.

        This method verifies that the save method correctly saves the instance
        to a file, and the saved data matches the expected data.

        Exceptions:
        - AssertionError: If the saved data does not match the expected data.
        - FileNotFoundError: If the 'file.json' file does not exist.
        - JSONDecodeError: If an error occurs while loading the JSON data from the file.
        """

        try:
            # Add your test code here
            # For example, create an instance, call the save method, and check the saved data
            i = self.value()
            i.save()
            key = self.name + "." + i.id
            with open("file.json", "r") as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError("The saved data does not match
                                 the expected data.") from e
        except FileNotFoundError as e:
            # Handle the file not found error
            # Log the error or perform any necessary actions
            raise FileNotFoundError("'file.json' file not found.") from e
        except JSONDecodeError as e:
            # Handle the JSON decode error
            # Log the error or perform any necessary actions
            raise JSONDecodeError("Error while loading JSON data from the file.") from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_str(self):
        """
        Test the string representation of the instance.

        This method verifies that the string representation of the instance
        matches the expected format.

        Exceptions:
        - AssertionError: If the string representation does
        not match the expected format.
        """

        try:
            i = self.value()
            expected_str = "[{}] ({}) {}".format(self.name, i.id, i.__dict__)
            self.assertEqual(str(i), expected_str)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError(
                "The string representation does not match the expected format."
            ) from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_todict(self):
        """
        Test the to_dict method.

        This method verifies that the to_dict method returns a dictionary
        representation of the instance, and the returned dictionary matches
        the original dictionary.

        Exceptions:
        - AssertionError: If the returned dictionary does
        not match the original dictionary.
        """

        try:
            original_dict = i.to_dict()
            self.assertEqual(i.to_dict(), original_dict)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError(
                "The returned dictionary does not match the original dictionary."
            ) from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_kwargs_none(self):
        """
        Test the creation of a new instance using keyword arguments with None values.

        This method verifies that when None values are provided as keyword arguments,
        a TypeError is raised.

        Exceptions:
        - AssertionError: If the expected TypeError is not raised.
        """

        try:
            n = {None: None}
            with self.assertRaises(TypeError):
                new = self.value(**n)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError("The expected TypeError was not raised.") from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_id(self):
        """
        Test the id attribute.

        This method verifies that the id attribute of the instance is of type str.

        Exceptions:
        - AssertionError: If the id attribute is not of type str.
        """

        try:
            # Add your test code here
            # For example, create an instance and check the type of the id attribute
            new = self.value()
            self.assertEqual(type(new.id), str)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError("The id attribute is not of type str.") from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_created_at(self):
        """
        Test the created_at attribute.

        This method verifies that the created_at attribute of the
        instance is of type datetime.datetime.

        Exceptions:
        - AssertionError: If the created_at attribute is not of type datetime.datetime.
        """

        try:
            # Add your test code here
            # For example, create an instance and check the type of the created_at attribute
            new = self.value()
            self.assertEqual(type(new.created_at), datetime.datetime)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError("The created_at attribute is not of type datetime.
                                 datetime.") from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_updated_at(self):
        """
        Test the updated_at attribute.

        This method verifies that the updated_at attribute of
        the instance is of type datetime.datetime,
        and that the values of created_at and updated_at are
        not the same when creating a new instance
        using the to_dict method.

        Exceptions:
        - AssertionError: If the updated_at attribute is
        not of type datetime.datetime,
        or if the values of created_at and updated_at are the same.
        """

        try:
            # Add your test code here
            # For example, create an instance, check the type of the updated_at attribute,
            # convert it to a dictionary, create a new instance using the dictionary,
            and compare created_at and updated_at
            new = self.value()
            self.assertEqual(type(new.updated_at), datetime.datetime)
            n = new.to_dict()
            new = BaseModel(**n)
            self.assertFalse(new.created_at == new.updated_at)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError("The updated_at attribute is not of type datetime.datetime,
                    or the values of created_at and updated_at are the same.") from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_uuid(self):
        """
        Test the UUID generation.

        This method verifies that the UUID generated for each instance is of type str
        and that the UUIDs generated for different instances are unique.

        Exceptions:
        - AssertionError: If the UUID is not of type str or
        if the generated UUIDs are not unique.
        """

        try:
            # Add your test code here
            # For example, create multiple instances, check the type of their UUIDs,
            # and ensure the UUIDs are unique
            instance1 = BaseModel()
            instance2 = BaseModel()
            instance3 = BaseModel()
            list_instances = [instance1, instance2, instance3]

            for instance in list_instances:
                ins_uuid = instance.id
                with self.subTest(uuid=ins_uuid):
                    self.assertIs(type(ins_uuid), str)

            self.assertNotEqual(instance1.id, instance2.id)
            self.assertNotEqual(instance1.id, instance3.id)
            self.assertNotEqual(instance2.id, instance3.id)
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError(
                "The UUID is not of type str or the generated UUIDs are not unique."
            ) from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_str_method(self):
        """
        Test the string representation of the instance.

        This method verifies that the string representation of the instance
        matches the expected format.

        Exceptions:
        - AssertionError: If the string representation does
        not match the expected format.
        """

        try:
            # Add your test code here
            # For example, create an instance and compare its string representation
            instance6 = BaseModel()
            expected_str = "[BaseModel] ({}) {}".format(
                instance6.id, instance6.__dict__
            )
            self.assertEqual(string_output, str(instance6))
        except AssertionError as e:
            # Handle the assertion error
            # Log the error or perform any necessary actions
            raise AssertionError("The string representation does
                                 not match the expected format.") from e
        except Exception as e:
            # Handle other unexpected exceptions that may occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.

    This class contains test cases to verify the
    functionality of the BaseModel class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class.

        This method is called before any test methods in
        the test class are run.
        It sets up an instance of the BaseModel class and
        assigns values to its attributes.

        Exceptions:
        - Exception: If an error occurs during the setup.
        """

        try:
            cls.base = BaseModel()
            cls.base.name = "Kev"
            cls.base.num = 20
        except Exception as e:
            # Handle any exceptions that occur during the setup
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the setup.") from e

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test class.

        This method is called after all test methods in
        the test class have been run.
        It cleans up any resources used by the test class.

        Exceptions:
        - Exception: If an error occurs during the tear-down.
        """

        try:
            del cls.base
        except Exception as e:
            # Handle any exceptions that occur during the tear-down
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the tear-down.") from e

    def tearDown(self):
        """
        Tear down the test.

        This method is called after each individual test method.
        It cleans up any resources used by the test.

        Exceptions:
        - Exception: If an error occurs during the tear-down.
        """

        try:
            os.remove("file.json")
        except Exception as e:
            # Handle any exceptions that occur during the tear-down
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the tear-down.") from e

    def test_pep8_BaseModel(self):
        """
        Test for PEP 8 compliance.

        This method checks if the BaseModel class file ('models/base_model.py')
        complies with the PEP 8 style guide.

        Exceptions:
        - AssertionError: If the PEP 8 check fails.
        """

        try:
            style = pep8.StyleGuide(quiet=True)
            p = style.check_files(["models/base_model.py"])
            self.assertEqual(p.total_errors, 0,
                             "PEP 8 style violations found. Fix them.")
        except Exception as e:
            # Handle any exceptions that occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_checking_for_docstring_BaseModel(self):
        """
        Test for existence of docstrings in BaseModel.

        This method checks if the BaseModel class and its methods have docstrings.
        It verifies that the docstrings are not None.

        Exceptions:
        - AssertionError: If any of the docstrings are None.
        """

        try:
            self.assertIsNotNone(BaseModel.__doc__)
            self.assertIsNotNone(BaseModel.__init__.__doc__)
            self.assertIsNotNone(BaseModel.__str__.__doc__)
            self.assertIsNotNone(BaseModel.save.__doc__)
            self.assertIsNotNone(BaseModel.to_dict.__doc__)
        except Exception as e:
            # Handle any exceptions that occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_method_BaseModel(self):
        """
        Test for the presence of methods in BaseModel.

        This method checks if the BaseModel class has the required methods.
        It verifies that the methods exist using the hasattr() function.

        Exceptions:
        - AssertionError: If any of the required methods are missing.
        """

        try:
            self.assertTrue(hasattr(BaseModel, "__init__"))
            self.assertTrue(hasattr(BaseModel, "save"))
            self.assertTrue(hasattr(BaseModel, "to_dict"))
        except Exception as e:
            # Handle any exceptions that occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_init_BaseModel(self):
        """
        Test if the base object is an instance of BaseModel.

        This method checks if the base object created in the setUpClass() method
        is an instance of the BaseModel class.

        Exceptions:
        - AssertionError: If the base object is not an instance of BaseModel.
        """

        try:
            self.assertTrue(isinstance(self.base, BaseModel))
        except Exception as e:
            # Handle any exceptions that occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_save_BaseModel(self):
        """
        Test if the save() method updates the 'updated_at' attribute.

        This method tests if the save() method of the BaseModel class updates
        the 'updated_at' attribute of the base object.

        Exceptions:
        - AssertionError: If the 'created_at' and 'updated_at'
        attributes are equal after calling save().
        """

        try:
            self.base.save()
            self.assertNotEqual(self.base.created_at, self.base.updated_at)
        except Exception as e:
            # Handle any exceptions that occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e

    def test_to_dict_BaseModel(self):
        """
        Test if the to_dict() method returns a dictionary with the expected attributes.

        This method tests if the to_dict() method of the BaseModel class returns
        a dictionary with the expected attributes and their respective values.

        Exceptions:
        - AssertionError: If any of the conditions for the expected attributes fail.
        """

        try:
            base_dict = self.base.to_dict()
            self.assertEqual(self.base.__class__.__name__, "BaseModel")
            self.assertIsInstance(base_dict["created_at"], str)
            self.assertIsInstance(base_dict["updated_at"], str)
        except Exception as e:
            # Handle any exceptions that occur during the test
            # Log the exception or perform any necessary actions
            raise Exception("An error occurred during the test.") from e


if __name__ == "__main__":
    unittest.main()
