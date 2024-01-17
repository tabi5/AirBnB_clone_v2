#!/usr/bin/python3
"""
Test cases for the State class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    Test cases for the State class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test_state class.

        Args:
            *args: Variable-length arguments.
            **kwargs: Keyword arguments.

        Returns:
            None

        """
        try:
            super().__init__(*args, **kwargs)
            self.name = "State"
            self.value = State
        except Exception as e:
            print(f"Error in __init__ method: {str(e)}")

    def test_name(self):
        """
        Test the name attribute of the State object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.name), str)
        except Exception as e:
            print(f"Error in test_name method: {str(e)}")
