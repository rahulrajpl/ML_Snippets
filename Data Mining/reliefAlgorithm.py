from sklearn import preprocessing
import pandas as pd
import numpy as np

def Top_two_features(dataframe):
    """
    Function calculates the scores of each data element in the dataframe
    and returns a 2 element tuple of indices of  highest and second highest feature of dataframe

    Usage: Top_two_features(df)

    Return Value: (a, b) # a will be highest and b will be second highest

    """
    scores = []
    d = dataframe
    for x in range(len(d.columns)):
        nmiss = []
        nhit = []
        s = 0
        # Finding Nearmiss value
        for i in d[d.columns[x]]:
            nmiss.append(min(sorted([np.linalg.norm(i - j) for j in d.iloc[x]])[1:]))
        # Finding NearHit value
        for k in d[d.columns[x]]:
            nhit.append(min(sorted([np.linalg.norm(k - l) for l in d[d.columns[x]]])[1:]))
            # Calculating the scores of the feature
        for i in range(len(nmiss)):
            s -= nhit[i] + nmiss[i]
        scores.append(s)
    # Feature with highest score is
    f1 = scores.index(max(sorted(scores)))
    # Feature with second highest score is
    f2 = scores.index(max(sorted(scores)[:-1]))
    return (f1, f2)
