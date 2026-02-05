import os
from dotenv import load_dotenv
load_dotenv()
URI = os.getenv("URI")
#print(URI)
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','default-dev-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = URI
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = URI
    DEBUG = False