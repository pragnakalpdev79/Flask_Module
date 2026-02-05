from app import create_app
from config import DevConfig

application = create_app(DevConfig)

if __name__ == "__main__":
    application.run(debug=True)

    