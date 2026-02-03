from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() #creates the db object usig constructor
migrate = Migrate()
#NOT CONNECTED TO ANY APP YET,JUST CONSTRUCTOR OBJECTS