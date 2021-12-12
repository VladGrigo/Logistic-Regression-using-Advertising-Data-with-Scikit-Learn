#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__, template_folder="templates")

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
    #return "Hello World"

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,5)
    loaded_model = pickle.load(open("advertising_model.sav","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        
        if int(result)==1:
            prediction='Profile likely to click the Mobile Ad'
        else:
            prediction='Profile less likely to click the Mobile Ad'
            
        return render_template("result.html",prediction=prediction)

if __name__ == "__main__":
	app.run(debug=True)