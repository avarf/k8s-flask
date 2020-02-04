import os
import subprocess
import shutil
import sys

from flask import Flask, request
from flask import send_file

import base64
import requests

import logging
import pprint

import random
import json


# logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__file__)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler(sys.stderr))
LOG.handlers[0].formatter = logging.Formatter('[%(levelname)s] %(message)s')


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'HELLO! Flask is up.'

if __name__ == '__main__':
    # starting flask and listening for requests
    app.run(debug=True, host='0.0.0.0')
