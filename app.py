# MUST upgrade pip on local env = "pip install --upgrade pip"  , so that skilearn installs

import flask
import pandas as pd
import joblib

filename = 'model/bike_model.sav'

# Use joblib / pickle doesnt work to load in the pre-trained model
model = joblib.load(filename)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return flask.render_template('main.html')

@app.route('/imageclassifier')
def imageclassifier():
    return flask.render_template('instruments_newformat.html')


@app.route('/dataanalysis', methods=['GET', 'POST'])

def dataanalysis():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('pandas.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        temperature = flask.request.form['temperature']
        humidity = flask.request.form['humidity']
        windspeed = flask.request.form['windspeed']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[temperature, humidity, windspeed]],
                                       columns=['temperature', 'humidity', 'windspeed'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('pandas.html',
                                     original_input={'Temperature':temperature,
                                                     'Humidity':humidity,
                                                     'Windspeed':windspeed},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()