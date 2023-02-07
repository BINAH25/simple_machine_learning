# importing modules
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
#from sklearn.externals import joblib
import joblib

# variables
data = pd.read_csv('sport_data.csv')
# replacing female and male with o and 1
data.replace(['Female','Male'],[0,1],inplace=True)
# droping the Sport column
x = data.drop(columns='Sport')
y = data.drop(columns=['Age','Height','Sex'])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

# Building machine learning Model
clf = DecisionTreeClassifier()
clf.fit(x_train,y_train)

# testing the machine learning model
test = clf.predict(x_test)
# ckecking for efficacy
accuracy = accuracy_score(y_test,test)
print(accuracy)
joblib.dump(clf,'ml_sport_model.joblib')

