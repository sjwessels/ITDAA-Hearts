import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with sqlite3.connect('hearts.db') as conn:
    query = "SELECT * FROM hearts"
    df = pd.read_sql(query, conn)

numeric_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=column, hue='target', kde=True, bins=20, alpha=0.7)
    plt.title(f'Distribution of {column} by Target')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.legend(title='Target', loc='upper right', labels=['No Disease', 'Disease'])
    plt.show()
