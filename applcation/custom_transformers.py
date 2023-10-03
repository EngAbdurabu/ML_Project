from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder

class MultiColumnLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = columns  # list of column names to encode

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        output = X.copy()
        for col in self.columns:
            le = LabelEncoder()
            output[col] = le.fit_transform(output[col].astype(str))  # Ensure data type is string
        return output
