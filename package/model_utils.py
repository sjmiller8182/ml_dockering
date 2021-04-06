
from typing import Callable

from numpy import ndarray
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def validate_model(X_test, y_test, model, metric: Callable):
    """
    """
    preds = model.predict(X_test)
    return metric(y_test, preds)

def train_model(
    X: ndarray,
    y: ndarray,
    params: dict = None,
    validation_data: tuple = None, 
    metric: Callable = accuracy_score,
    search: bool = False,
    n_jobs = None) -> dict:
    """
    """
    
    results = {}

    rf = RandomForestClassifier(n_jobs=n_jobs)

    if not search:
        if params:
            rf.set_params(**params)
        rf.fit(X, y)
    else:
        raise NotImplementedError("Currently model hyperparameter search is not implemented")

    results['model'] = rf

    if validation_data:
        results['val_perf'] = validate_model(*validation_data, rf, metric)

    return results

