from flask import Flask
from extensions import db,migrate
from models import Author,Book

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app,db)

    return app 

if __name__ == '__main__':
    app = create_app()
    author = Author(name="JK RoW",bio="british")
    db.session.add(author)
    db.session.commit()

    book1 = Book(title="Harry Potter", price=19.99, author_id=author.id)
    book2 = Book(title="Fantastic Beasts", price=15.99, author_id=author.id)
    db.session.add_all([book1, book2])
    db.session.commit()


    print(author.books)  # [<Book Harry Potter>, <Book Fantastic Beasts>]
    print(book1.author)  # <Author J.K. Rowling>

    db.session.delete(author)
    db.session.commit()
    app.run(debug=True)
    


