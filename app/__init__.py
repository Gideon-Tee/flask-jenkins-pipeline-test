from flask import Flask
from app.blueprints import web

app = Flask(__name__)


app.register_blueprint(web.bp)