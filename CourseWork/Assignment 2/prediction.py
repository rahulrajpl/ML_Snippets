"""prediction.py - Implementation of Decision Tree Classifier."""

__author__ = "Rahul Raj"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Be one. Get in touch through email>"
__email__ = "rahulr@iitk.ac.in"
__status__ = "Development"


from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

data = pd.read_csv('data_18111053.csv')
data1 = pd.read_csv('./data_class_5.csv') # Additional points of class 5
data2 = pd.read_csv('./data_random_class.csv') # Additional random points and its classes

# Separating the input data to variable 'd'
d = []
for i,j,z in zip(data['x1'],data['x2'],data['x3']):
    d.append([i,j,z])
d =np.array(d)

# Getting the target_class of each input data to variable 'target'
target = []
for i in range(90):
    target.append(int(data.iloc[i]['class']))
target = np.array(target)

X_train, X_test, y_train, y_test = train_test_split(d, target, test_size = .3, random_state = 0,stratify=target)

depth = 6
dtree_model = DecisionTreeClassifier(max_depth=depth).fit(X_train, y_train)
dtree_predictions = dtree_model.predict(X_test)
# cm = confusion_matrix(y_test, dtree_predictions)
print('Accuracy when depth is', depth, '=', str(accuracy_score(y_test, dtree_predictions)))

# Appending 10 more datapoints obtained to original collection and training again
data =pd.concat([data,data1,data2])

# Separating the input data to variable 'd'
d = []
for i,j,z in zip(data['x1'],data['x2'],data['x3']):
    d.append([i,j,z])
d =np.array(d)

# Getting the target_class of each input data to variable 'target'
target = []
for i in range(100):
    target.append(int(data.iloc[i]['class']))
target = np.array(target)

X_train, X_test, y_train, y_test = train_test_split(d, target, test_size = .15, random_state = 0,stratify=target)

# Training DT Model
depth = 5
dtree_model = DecisionTreeClassifier(max_depth=depth).fit(X_train, y_train)
dtree_predictions = dtree_model.predict(X_test)
# cm = confusion_matrix(y_test, dtree_predictions)
print('Accuracy when depth is', depth, '=', str(accuracy_score(y_test, dtree_predictions)))

# Testing random class
rc = pd.read_csv('./data_random_class.csv')
r = np.array(rc.iloc[:,:3])
print(list(dtree_model.predict(r)),'<-Predicted classes -')
print(list(rc['class']),'<-Actual classes -')

# Testing class 5 data
r5 = pd.read_csv('./data_class_5.csv')
t = np.array(r5.iloc[:,:3])
print(list(dtree_model.predict(t)),'<-Predicted classes -')
print(list(r5['class']),'<-Actual classes -')

print('end')
