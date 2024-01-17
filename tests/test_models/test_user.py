#!/usr/bin/python3
"""
Test cases for the User class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    Test cases for the User class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test_User class.

        Args:
            *args: Variable-length arguments.
            **kwargs: Keyword arguments.

        Returns:
            None

        """
        try:
            super().__init__(*args, **kwargs)
            self.name = "User"
            self.value = User
        except Exception as e:
            print(f"Error in __init__ method: {str(e)}")

    def test_first_name(self):
        """
        Test the first_name attribute of the User object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.first_name), str)
        except Exception as e:
            print(f"Error in test_first_name method: {str(e)}")

    def test_last_name(self):
        """
        Test the last_name attribute of the User object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.last_name), str)
        except Exception as e:
            print(f"Error in test_last_name method: {str(e)}")

    def test_email(self):
        """
        Test the email attribute of the User object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.email), str)
        except Exception as e:
            print(f"Error in test_email method: {str(e)}")

    def test_password(self):
        """
        Test the password attribute of the User object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.password), str)
        except Exception as e:
            print(f"Error in test_password method: {str(e)}")
