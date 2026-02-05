from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

pw_hash = bcrypt.generate_password_hash('secret').decode('utf-8')

is_valid = b