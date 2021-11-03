#from flask_mysqldb import MySQL,MySQLdb  

from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_cors import CORS
from app import app
#A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
#Axios doesnt work without this
from app.src.Disease import predictDisease

CORS(app)

#######################################################
##################''' Controllers '''##################
#######################################################
@app.route("/")
def test():
    return {"members":["Member","Hello Sandaruwan"]}

@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == 'POST':
        # if request.get_json()['msg'] == "Hi":
        re = predictDisease(request.get_json()['diseases'])
        return {"members": re}

