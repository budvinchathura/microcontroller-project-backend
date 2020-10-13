from flask import Flask
from app.home import HOME_BP
from app.submit import SUBMIT_BP
APP = Flask(__name__)

APP.register_blueprint(HOME_BP, url_prefix='/')
APP.register_blueprint(SUBMIT_BP, url_prefix='/submit-data')
