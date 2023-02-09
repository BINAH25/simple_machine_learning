from sklearn.tree import DecisionTreeClassifier
import joblib


model = joblib.load('ml_sport_model.joblib')
new_student = model.predict([[15,4,1]])
print(new_student)