from config import config
import requests
from flask import request, jsonify, Flask

app = Flask(__name__)
config = config()
