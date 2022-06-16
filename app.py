from crypt import methods
import flask
from flask import render_template
import pickle
import sklearn
import tensorflow
from tensorflow import keras
print("Hello world!")

app=flask.Flask(__name__, template_folder='template1')

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open('dnn_model.pkl', 'rb') as f:
            loaded_model=pickle.load(f)

        train_feature=float(flask.request.form['Количество отвердителя. м.%'])
        y_pred=loaded_model.predict([[train_feature]])

        return render_template('main.html', result = y_pred)

if __name__== '__main__':
    app.run()

        