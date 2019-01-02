from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split, KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import *
import pickle
import pandas as pd
import numpy as np

from k_fold_validation import KFoldValidation

model_cat = "ssh"

#reading csv data
colum =['user','is_private','is_failure','is_root','is_valid','not_valid_count','ip_failure','ip_success','no_failure','first','td','ts','class']

csv = pd.read_csv("data/SSH.csv",)
df = pd.DataFrame(csv,columns=colum)

#slice and dice.
df.pop('user')
df.pop('ts')
df.pop('td')
print(df)
label = np.array(df.pop("class"))
features = np.array(df)
X_train,X_test,y_train,y_test = train_test_split(features,label,shuffle=True,random_state=22)

#training model
print("Training Model..")
model = GaussianNB()
model.fit(X_train,y_train)

#saving model using pickle
m_name="gnb"
pkl_filename="models/"+model_cat+"_"+m_name+'.pkl'
with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)

#accuracy calculation
print("Train Accuracy : ", model.score(X_train, y_train))
print("Test Accuracy : ", model.score(X_test, y_test))

#testing data through perdiction
perdict = model.predict([X_test[20]])
print(perdict)
print(y_test[20])

try:
    # confusion matrix
    y_pred = model.fit(X_train, y_train).predict(X_test)
    cnf_matrix = confusion_matrix(y_test, y_pred)
    print(cnf_matrix)
except:
    y_pred = model.fit(X_train.round(), y_train.round()).predict(X_test.round())
    cnf_matrix = confusion_matrix(y_test.round(), y_pred.round())
    print(cnf_matrix)

kf = KFoldValidation()
kf.GetAverageScore(10,features,label,GaussianNB(),X_train)