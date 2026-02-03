''' 
Using the db.Model class to define models
it handles Flask-SQLAlchemy's bind keys to associate with a specific engine
a bind key is a short string that asscoiate each engine with a string,and then with model
the session choes what enginer to use for query based on the bind key
'''

from extensions import db #the sqlalchemy object from extension not the app

#Defining a model does not create it in the database. 
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)