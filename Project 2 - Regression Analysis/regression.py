import quandl, math
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# SVM is Support Vector Machine

df = quandl.get("WIKI/GOOGL", authtoken="y5FErz9PVcHDyDSyFL__")
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

# To shift the column element up, we are using -ve sign
df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)

# X are features and Y are Labels

X = np.array(df.drop(['label']), 1)
Y = np.array(df['label'])

# Now we are going to scale X by preprocessing
X = preprocessing.scale(X) # scaling or normalising before feeding to classifier
X = X[:-forecast_out+1]
df.dropna(inplace=True)
Y = np.array(df['label'])

print(len(X), len(Y))
