import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import json
#rom flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import urllib.request

app = Flask(__name__)
CORS(app)

@app.route('/version', methods=['GET'])
def version():
    if  os.path.exists("version.txt"):
        with open("version.txt", 'r') as f:
            a = f.read()
            return(a)
    else:
        return "0"

        # main
if __name__ == '__main__':
    app.run('10.26.1.228', 5010, debug=True)
