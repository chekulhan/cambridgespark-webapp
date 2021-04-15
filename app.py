import flask
#import pickle5 as pickle
#import pandas as pd

# Use pickle to load in the pre-trained model
#with open(f'model/bike_model_xgboost.pkl', 'rb') as f:
#    model = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__)

# Set up the main route
@app.route('/')
def main():
    print("It works")

if __name__ == '__main__':
    app.run()
