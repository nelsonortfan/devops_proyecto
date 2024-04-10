from flask import Flask, jsonify
from .models import db
from flask_restful import Api
from .views import BlackListView
from dotenv import load_dotenv
import os


def create_app(config_name):
    application = Flask(__name__)    
    load_dotenv('env.development')
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_name = os.environ.get("DB_NAME")
    db_uri = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    application.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return application

application = create_app('default')


db.init_app(application)

api = Api(application)

api.add_resource(BlackListView, '/blacklists')



if __name__ == "__main__":
    with application.app_context():
        db.create_all()
        application.run(port = 3000, debug = True)
        app_context = application.app_context()
        app_context.push()
    