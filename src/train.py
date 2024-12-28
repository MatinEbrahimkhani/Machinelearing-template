from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def train_model(X_train, y_train, model_type='logistic_regression'):
    """Train a machine learning model based on the specified type."""
    if model_type == 'logistic_regression':
        model = LogisticRegression()
    elif model_type == 'random_forest':
        model = RandomForestClassifier()
    elif model_type == 'svm':
        model = SVC()
    else:
        raise ValueError(f"Model type {model_type} is not supported.")

    model.fit(X_train, y_train)
    return model
