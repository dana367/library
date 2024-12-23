from app import create_app
from flask import Flask
from flask_cors import CORS

application = create_app()
CORS(application)

if __name__ == "__main__":
    application.run(debug=True)
