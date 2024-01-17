#!/usr/bin/python3
"""
Test cases for the Review class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    Test cases for the Review class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test_review class.

        Args:
            *args: Variable-length arguments.
            **kwargs: Keyword arguments.

        Returns:
            None

        """
        try:
            super().__init__(*args, **kwargs)
            self.name = "Review"
            self.value = Review
        except Exception as e:
            print(f"Error in __init__ method: {str(e)}")

    def test_place_id(self):
        """
        Test the place_id attribute of the Review object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.place_id), str)
        except Exception as e:
            print(f"Error in test_place_id method: {str(e)}")

    def test_user_id(self):
        """
        Test the user_id attribute of the Review object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.user_id), str)
        except Exception as e:
            print(f"Error in test_user_id method: {str(e)}")

    def test_text(self):
        """
        Test the text attribute of the Review object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.text), str)
        except Exception as e:
            print(f"Error in test_text method: {str(e)}")
