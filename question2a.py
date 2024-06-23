import sqlite3
import pandas as pd

with sqlite3.connect('hearts.db') as conn:
    query = "SELECT * FROM hearts"
    df = pd.read_sql(query, conn)
    
missingValues = df.isnull().sum()
print("missing value:\n", missingValues)

numericColumns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

df[numericColumns] = df[numericColumns].apply(pd.to_numeric, errors='coerce')

df.fillna(df.mean(), inplace=True)
