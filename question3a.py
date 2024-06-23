import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split


with sqlite3.connect('hearts.db') as conn:
    query = "SELECT * FROM hearts"
    df = pd.read_sql(query, conn)

X = df.drop(columns=['target'])
y = df['target']

categorical_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
