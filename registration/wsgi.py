from app import create_app
from config import DevConfig

application = create_app(DevConfig)

if __name__ == "__main__":
    print("Starting the app!!!!!!!!!!!!!!")
    application.run(debug=True)

    