import pandas as pd
import sqlite3

df = pd.read_csv("C:/Users/User/Desktop/ITDAA/ITDAA Assignment/heart.csv", sep=";")


conn = sqlite3.connect('hearts.db')
cur = conn.cursor()
try:
    cur.execute('''CREATE TABLE hearts(
                age INT , 
                sex BOOLEAN,
                cp INT, 
                trestbps INT, 
                chol INT, 
                fbs BOOLEAN, 
                restecg INT,
                thalach INT,
                exang BOOLEAN,
                oldpeak REAL,
                slope INT,
                ca INT,
                thal INT, 
                target BOOLEAN
                )''')
    
except: 
  print("Table exists")    

df.to_sql('hearts',conn,if_exists='append',index=False)
