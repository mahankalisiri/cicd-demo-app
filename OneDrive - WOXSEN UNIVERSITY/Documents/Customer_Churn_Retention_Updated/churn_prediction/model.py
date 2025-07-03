from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class ChurnPredictor:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def predict(self, X):
        return self.model.predict_proba(X)[:, 1]
