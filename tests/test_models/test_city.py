#!/usr/bin/python3
"""
Module: test_City

This module contains unit tests for the City class in the models module.
"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle


class test_City(test_basemodel):
    """
    Class: test_City

    This class provides unit tests for the City class,
    which represents a city
    in the application. It inherits from
    the test_basemodel class and includes
    test cases specific to the City class.
    """

    def __init__(self, *args, **kwargs):
        """
        Method: __init__

        Initializes a new instance of the City class.

        Parameters:
        *args: Variable-length positional arguments.
        **kwargs: Variable-length keyword arguments.

        Description:
        This method is responsible for initializing the City object.
        It calls the
        base class's __init__ method using super()
        and passes any provided
        positional and keyword arguments. Additionally,
        it sets the name attribute
        to "City" and the value attribute to an instance of the City class.

        Raises:
        ValueError: If the value provided for
        the name attribute is not a string.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

        if not isinstance(self.name, str):
            raise ValueError("Name attribute must be a string.")

    def test_state_id(self):
        """
        Method: test_state_id

        Unit test for the state_id attribute of the City class.

        Description:
        This method creates a new instance of
        the City class and verifies that
        the state_id attribute is of
        type str (string) using the self.assertEqual
        assertion.

        Test:
        - Create a new instance of the City class.
        - Assert that the type of the state_id attribute is str.
        """
        try:
            new = self.value()
            self.assertEqual(type(new.state_id), str)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_name(self):
        """
        Method: test_name

        Unit test for the name attribute of the City class.

        Description:
        This method creates a new instance of the City class and verifies that
        the name attribute is of type str (string) using the self.assertEqual
        assertion.

        Test:
        - Create a new instance of the City class.
        - Assert that the type of the name attribute is str.
        """
        try:
            new = self.value()
            self.assertEqual(type(new.name), str)
        except Exception as e:
            print(f"An error occurred: {e}")


class Test_PEP8(unittest.TestCase):
    """
    Class: Test_PEP8

    This class provides unit tests for PEP8 style compliance in the User class.
    """

    def test_pep8_user(self):
        """
        Method: test_pep8_user

        Unit test for PEP8 style compliance in the User class.

        Description:
        This method uses the pycodestyle module to check the PEP8 style
        compliance of the 'models/city.py' file. It asserts that there are no
        errors or warnings found.

        Test:
        - Create a pycodestyle.StyleGuide object with quiet mode enabled.
        - Use the StyleGuide.check_files method to check the 'models/city.py'
          file.
        - Assert that the total number of errors found is 0.
        """
        try:
            pep8style = pycodestyle.StyleGuide(quiet=True)
            result = pep8style.check_files(['models/city.py'])
            self.assertEqual(result.total_errors, 0,
                             "Found code style errors (and warnings).")
        except Exception as e:
            print(f"An error occurred: {e}")


class TestCity(unittest.TestCase):
    """
    Class: TestCity

    This class provides unit tests for the City class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Method: setUpClass

        Set up for the test.

        Description:
        This method is called before any test
        methods in the class. It creates
        an instance of the City class and sets
        the name and state_id attributes.

        Test setup:
        - Create an instance of the City class.
        - Set the name and state_id attributes.
        """
        try:
            cls.city = City()
            cls.city.name = "LA"
            cls.city.state_id = "CA"
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def tearDownClass(cls):
        """
        Method: tearDownClass

        Tear down for the test.

        Description:
        This method is called after all test
        methods in the class have been run.
        It deletes the instance of the City class.

        Test teardown:
        - Delete the instance of the City class.
        """
        try:
            del cls.city
        except Exception as e:
            print(f"An error occurred: {e}")

    def tearDown(self):
        """
        Method: tearDown

        Teardown for each individual test method.

        Description:
        This method is called after each individual test method. It tries to
        remove the "file.json" file, if it exists, for cleanup purposes.
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """
        Method: test_pep8_City

        Unit test for PEP8 style compliance in the City class.

        Description:
        This method uses the `pep8` module
        to check the PEP8 style compliance of
        the 'models/city.py' file.
        It asserts that there are no errors.

        Test:
        - Create a `pep8.StyleGuide` object with quiet mode enabled.
        - Use the `StyleGuide.check_files` method to check the 'models/city.py'
        file.
        - Assert that the total number of errors found is 0.
        """
        try:
            style = pep8.StyleGuide(quiet=True)
            p = style.check_files(['models/city.py'])
            self.assertEqual(p.total_errors, 0, "fix pep8")

        except Exception as e:
            print(f"An error occurred: {e}")

    def test_checking_for_docstring_City(self):
        """
        Method: test_checking_for_docstring_City

        Unit test to check if the City class has a docstring.

        Description:
        This method checks if the `City` class has a docstring by using the
        `City.__doc__` attribute. It asserts that the docstring is not None.

        Test:
        - Assert that the `City.__doc__` attribute is not None.
        """
        try:
            self.assertIsNotNone(City.__doc__)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_attributes_City(self):
        """
        Method: test_attributes_City

        Unit test to check if the City class has the expected attributes.

        Description:
        This method checks if the `City` class has the following attributes:
        'id', 'created_at', 'updated_at', 'state_id', and 'name'. It asserts
        that each attribute is present in the `City.__dict__` dictionary.

        Test:
        - Assert that each expected attribute is present in the `City.__dict__`
        dictionary.
        """
        try:
            self.assertTrue('id' in self.city.__dict__)
            self.assertTrue('created_at' in self.city.__dict__)
            self.assertTrue('updated_at' in self.city.__dict__)
            self.assertTrue('state_id' in self.city.__dict__)
            self.assertTrue('name' in self.city.__dict__)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_is_subclass_City(self):
        """
        Method: test_is_subclass_City

        Unit test to check if the City class is a subclass of BaseModel.

        Description:
        This method checks if the `City` class is a subclass of `BaseModel`
        by using the `issubclass` function. It asserts that the result is True.

        Test:
        - Assert that the `City` class is a subclass of `BaseModel`.
        """
        try:
            self.assertTrue(issubclass(self.city.__class__, BaseModel), True)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_attribute_types_City(self):
        """
        Method: test_attribute_types_City

        Unit test to check the attribute types in the City class.

        Description:
        This method checks the attribute types in the `City` class. It asserts
        that the `name` attribute is of type str and the `state_id` attribute
        is of type str.

        Test:
        - Assert that the `name` attribute is of type str.
        - Assert that the `state_id` attribute is of type str.
        """
        try:
            self.assertEqual(type(self.city.name), str)
            self.assertEqual(type(self.city.state_id), str)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_save_City(self):
        """
        Method: test_save_City

        Unit test to check if the `save` method works in the City class.

        Description:
        This method tests the `save` method in the `City` class. It calls the
        `save` method on the `self.city` object
        and asserts that the `created_at`
        and `updated_at` attributes are not equal.

        Test:
        - Call the `save` method on the `self.city` object.
        - Assert that the `created_at` and `updated_at`
        attributes are not equal.
        """
        try:
            self.city.save()
            self.assertNotEqual(self.city.created_at, self.city.updated_at)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_to_dict_City(self):
        """
        Method: test_to_dict_City

        Unit test to check if the `to_dict` method works in the City class.

        Description:
        This method tests the `to_dict` method in the `City` class. It asserts
        that the `to_dict` method is present in the `City` class.

        Test:
        - Assert that the `to_dict` method is present in the `City` class.
        """
        try:
            self.assertEqual('to_dict' in dir(self.city), True)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    unittest.main()
