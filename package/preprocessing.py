
import csv
from typing import Union

import numpy as np
from numpy import ndarray
from numpy.random import RandomState
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def read_data(path: str):
    """
    """
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        data = np.array(list(reader))
    return data[:, 1:], data[:, 0]

def preprocess(
    X: ndarray, 
    y: ndarray,
    random_state: Union[RandomState, int],
    test_size=0.33
    ) -> dict:
    """
    """
    # split the data as usual
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # scale data
    # fit on X_train
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    # apply on X_test
    X_test = scaler.transform(X_test)

    return {
        'data': (X_train, X_test, y_train, y_test),
        'scaler': scaler
    }

