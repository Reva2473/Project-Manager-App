from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017/')
client = MongoClient(MONGO_URI)
db = client.get_database('collabtask')

users_collection = db.users
projects_collection = db.projects
tasks_collection = db.tasks
