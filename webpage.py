
# import flask dependencies
from flask import Flask, request, make_response, jsonify, render_template
import requests
import json
from datetime import datetime


from werkzeug.debug import DebuggedApplication
# from gen_HTML import generate_HTML_report





app = Flask(__name__)
appDebug = DebuggedApplication(app, evalex=True)

# default route
@app.route('/')
def index():

    return render_template("gamepagecard.html")


# Host report 
@app.route('/fasit', methods=['GET'])
def report():
    return render_template('fasitpage.html')

# run the app
if __name__ == '__main__':
   app.run(debug=True)