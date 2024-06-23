import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


with sqlite3.connect('hearts.db') as conn:
    query = "SELECT * FROM hearts"
    df = pd.read_sql(query, conn)


categorical_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']


for column in categorical_columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=column, hue='target', data=df)
    plt.title(f'Distribution of {column} by Target')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.legend(title='Target', loc='upper right', labels=['No Disease', 'Disease'])
    plt.show()
