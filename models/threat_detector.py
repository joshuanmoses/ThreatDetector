from sklearn.ensemble import IsolationForest
import joblib
import numpy as np

class ThreatDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01)
    
    def train(self, X_train):
        self.model.fit(X_train)
    
    def predict(self, X_test):
        scores = self.model.decision_function(X_test)
        predictions = self.model.predict(X_test)
        return scores, predictions

    def save_model(self, path):
        joblib.dump(self.model, path)
    
    def load_model(self, path):
        self.model = joblib.load(path)

