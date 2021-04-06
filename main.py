
import os
import urllib.request
import csv

import yaml
from flask import Flask, request, jsonify
import numpy as np

from package.preprocessing import read_data, preprocess
from package.model_utils import train_model
from package.app_util import json_to_row

app = Flask(__name__)

DATA_PATH = './data/'
DATA_FILE = 'wine_data.csv'
random_state = np.random.RandomState(100)

# read in configuration
with open('./deploy/service_cfg.yaml', 'r') as cfg_file:
    cfg = yaml.safe_load(cfg_file)

# we are going to keep our base data here
if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)

# get the data
urllib.request.urlretrieve(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',
    filename=DATA_PATH + DATA_FILE
    )

# get data and preprecess
preprocessing = preprocess(
    *read_data(DATA_PATH + DATA_FILE), random_state
)

X_train, X_test, y_train, y_test = preprocessing['data']
scaler = preprocessing['scaler']

results = train_model(
    X_train, 
    y_train, 
    validation_data=(X_test, y_test),
    params=cfg.get('model_params', None)
    )

# ceate the app

# create service message on main page
@app.route('/')
def main_page():
    """
    Message printed at root to indicate the service is active
    """
    main_message = 'Model service is active.'

    if 'val_perf' in results:
        main_message += f'Validation performance: {0}.'

    return main_message

# create predict POST method
@app.route('/predict', methods=(['POST']))
def serve_model():
    content = request.get_data()
    data = json_to_row(content)
    data = scaler.transform(data)
    out = results['model'].predict(data)
    return jsonify({'score':out[0]})

host = cfg.get('app').get('host')
port = cfg.get('app').get('port')
if __name__ == '__main__':
    app.run(host=host, port=port)
