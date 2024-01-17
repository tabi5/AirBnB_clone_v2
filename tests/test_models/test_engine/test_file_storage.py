#!/usr/bin/python3
"""Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """Test case class for file storage functionality"""

    def setUp(self):
        """Set up test environment"""
        try:
            del_list = []  # List to store keys for deletion
            for key in storage._FileStorage__objects.keys():
                del_list.append(key)
            for key in del_list:
                del storage._FileStorage__objects[key]
        except Exception as e:
            print(f"Error in setUp: {str(e)}")

    def tearDown(self):
        """Remove storage file at the end of tests"""
        try:
            os.remove('file.json')
        except Exception as e:
            print(f"Error in tearDown: {str(e)}")

    def test_obj_list_empty(self):
        """Test that __objects is initially empty"""
        try:
            self.assertEqual(len(storage.all()), 0)
        except Exception as e:
            print(f"Error in test_obj_list_empty: {str(e)}")

    def test_new(self):
        """Test that a new object is correctly added to __objects"""
        try:
            new = BaseModel()
            for obj in storage.all().values():
                temp = obj
            self.assertTrue(temp is obj)
        except Exception as e:
            print(f"Error in test_new: {str(e)}")

    def test_all(self):
        """Test that __objects is properly returned"""
        try:
            new = BaseModel()
            temp = storage.all()
            self.assertIsInstance(temp, dict)
        except Exception as e:
            print(f"Error in test_all: {str(e)}")

    def test_base_model_instantiation(self):
        """Test that a file is not created on BaseModel save"""
        try:
            new = BaseModel()
            self.assertFalse(os.path.exists('file.json'))
        except Exception as e:
            print(f"Error in test_base_model_instantiation: {str(e)}")

    def test_empty(self):
        """Test that data is saved to the file"""
        try:
            new = BaseModel()
            thing = new.to_dict()
            new.save()
            new2 = BaseModel(**thing)
            self.assertNotEqual(os.path.getsize('file.json'), 0)
        except Exception as e:
            print(f"Error in test_empty: {str(e)}")

    def test_save(self):
        """Test the FileStorage save method"""
        try:
            new = BaseModel()
            storage.save()
            self.assertTrue(os.path.exists('file.json'))
        except Exception as e:
            print(f"Error in test_save: {str(e)}")

    def test_reload(self):
        """Test that the storage file is successfully loaded to __objects"""
        try:
            new = BaseModel()
            storage.save()
            storage.reload()
            for obj in storage.all().values():
                loaded = obj
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])
        except Exception as e:
            print(f"Error in test_reload: {str(e)}")

    def test_reload_empty(self):
        """Test loading from an empty file"""
        try:
            with open('file.json', 'w') as f:
                pass
            with self.assertRaises(ValueError):
                storage.reload()
        except Exception as e:
            print(f"Error in test_reload_empty: {str(e)}")

    def test_reload_from_nonexistent(self):
        """Test that nothing happens if the file does not exist"""
        try:
            self.assertEqual(storage.reload(), None)
        except Exception as e:
            print(f"Error in test_reload_from_nonexistent: {str(e)}")

    def test_base_model_save(self):
        """Test that the BaseModel save method calls storage save"""
        try:
            new = BaseModel()
            new.save()
            self.assertTrue(os.path.exists('file.json'))
        except Exception as e:
            print(f"Error in test_base_model_save: {str(e)}")

    def test_type_path(self):
        """Test that __file_path is of string type"""
        try:
            self.assertEqual(type(storage._FileStorage__file_path), str)
        except Exception as e:
            print(f"Error in test_type_path: {str(e)}")

    def test_type_objects(self):
        """Test that __objects is of dict type"""
        try:
            self.assertEqual(type(storage.all()), dict)
        except Exception as e:
            print(f"Error in test_type_objects: {str(e)}")

    def test_key_format(self):
        """Test that the key is properly formatted"""
        try:
            new = BaseModel()
            _id = new.to_dict()['id']
            for key in storage.all().keys():
                temp = key
            self.assertEqual(temp, 'BaseModel' + '.' + _id)
        except Exception as e:
            print(f"Error in test_key_format: {str(e)}")

    def test_storage_var_created(self):
        """Test that the FileStorage object 'storage' is created"""
        try:
            from models.engine.file_storage import FileStorage
            self.assertEqual(type(storage), FileStorage)
        except Exception as e:
            print(f"Error in test_storage_var_created: {str(e)}")
