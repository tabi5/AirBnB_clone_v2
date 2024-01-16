#!/usr/bin/python3
"""Create a unique FileStorage instance for your application"""

# Import necessary modules and classes
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

# Check the value of the environment variable HBNB_TYPE_STORAGE
# If it is set to "db", create a DBStorage instance; otherwise,
# create a FileStorage instance
var = "HBNB_TYPE_STORAGE"
if getenv(var) == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Load data from the storage system
storage.reload()
