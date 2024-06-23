import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
import pickle

with sqlite3.connect('hearts.db') as conn:
    query = "SELECT * FROM hearts"
    df = pd.read_sql(query, conn)

missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)

df.fillna(df.mean(), inplace=True)

X = df.drop(columns=['target'], axis = 1)
y = df['target']

Scaler = MinMaxScaler()

df = Scaler.fit_transform(df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2 , stratify= y)

pred_models = {
    "Random Forest Classifier": RandomForestClassifier(),
    "SVM": svm.SVC(kernel='linear'),
    "Gradient Boosting Classifier": GradientBoostingClassifier()
}

for name, pred_model in pred_models.items():
    pred_model.fit(X_train, y_train)
    predictions = pred_model.predict(X_test)
    print(f"{name} Accuracy: {accuracy_score(y_test, predictions)*100:.2f}%")
    
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train,y_train)

trainedModel = 'Prediction_model.sav'
pickle.dump(classifier, open(trainedModel, 'wb'))
print("Model Saved")
