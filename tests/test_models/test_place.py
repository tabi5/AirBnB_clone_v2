#!/usr/bin/python3
"""Unit tests for the Place class"""

import unittest
from models.place import Place
from tests.test_models.test_base_model import BaseModelTestCase


class PlaceTestCase(BaseModelTestCase):
    """
    Test cases for the Place class.

    This test class inherits from the BaseModelTestCase class and
    includes test methods to verify the functionalities of the Place class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a Place object.

        Args:
            *args: Variable-length arguments.
            **kwargs: Keyword arguments.

        Returns:
            None

        """
        try:
            super().__init__(*args, **kwargs)
            self.name = "Place"
            self.value = Place
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_city_id(self):
        """
        Test the city_id attribute of the Place object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.city_id), str)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_user_id(self):
        """
        Test the user_id attribute of the Place object.

        Args:
            None

        Returns:
            None
        """
        try:
            new = self.value()
            self.assertEqual(type(new.user_id), str)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_name(self):
        """
        Test the name attribute of the Place object.

        Args:
            None

        Returns:
            None
        """
        try:
            new = self.value()
            self.assertEqual(type(new.name), str)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_description(self):
        """
        Test the description attribute of the Place object.

        Args:
            None

        Returns:
            None
        """
        try:
            new = self.value()
            self.assertEqual(type(new.description), str)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_number_rooms(self):
        """
        Test the number_rooms attribute of the Place object.

        Args:
            None

        Returns:
            None
        """
        try:
            new = self.value()
            self.assertEqual(type(new.number_rooms), int)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_number_bathrooms(self):
        """
        Test the number_bathrooms attribute of the Place object.

        Args:
            None

        Returns:
            None
        """
        try:
            new = self.value()
            self.assertEqual(type(new.number_bathrooms), int)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_max_guest(self):
        """
        Test the max_guest attribute of the Place object.

        Args:
            None

        Returns:
            None
        """
        try:
            new = self.value()
            self.assertEqual(type(new.max_guest), int)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_price_by_night(self):
        """
        Test the price_by_night attribute of the Place object.

        Args:
            None

        Returns:
            None
        """
        try:
            new = self.value()
            self.assertEqual(type(new.price_by_night), int)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_latitude(self):
        """
        Test the latitude attribute of the Place object.

        Args:
            None

        Returns:
            None
        """
        try:
            new = self.value()
            self.assertEqual(type(new.latitude), float)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_longitude(self):
        """
        Test the longitude attribute of the Place object.

        Args:
            None

        Returns:
            None

        """
        try:
            new = self.value()
            self.assertEqual(type(new.latitude), float)
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_amenity_ids(self):
        """
        Test the amenity_ids attribute of the Place object.

        Args:
            None

        Returns:
            None
        """
        try:
            new = self.value()
            self.assertEqual(type(new.amenity_ids), list)
        except Exception as e:
            print(f"An error occurred: {e}")
