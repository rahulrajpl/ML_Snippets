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
        for i in range(d.shape[0]):
            s -= nhit[i] + nmiss[i]
        scores.append(s)
    # Feature with highest score is
    f1 = scores.index(max(sorted(scores)))
    # Feature with second highest score is
    f2 = scores.index(max(sorted(scores)[:-1]))
    return (f1, f2)


gdp_const_orig = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-constant-price.csv", nrows=1)
gdp_curr_orig = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-current-price.csv", nrows=1)
sw_gdp_const_orig = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-constant-price.csv", nrows=1)
sw_gdp_curr_orig = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-current-price.csv", nrows=1)

gdp_const = pd.read_csv("./output/Economy/gross-domestic-product-gdp-constant-price.csv", nrows=1)
gdp_curr = pd.read_csv("./output/Economy/gross-domestic-product-gdp-current-price.csv", nrows=1)
sw_gdp_const = pd.read_csv("./output/Economy/state-wise-net-domestic-product-ndp-constant-price.csv", nrows=1)
sw_gdp_curr = pd.read_csv("./output/Economy/state-wise-net-domestic-product-ndp-current-price.csv", nrows=1)

features = list(gdp_const_orig['Items Description'])+ list(gdp_curr_orig['Items  Description']) \
+ list(sw_gdp_const_orig['Item Description']) + list(sw_gdp_curr_orig['Item Description'])

df = pd.concat([gdp_const, gdp_curr,sw_gdp_const, sw_gdp_curr], sort=False)
df.drop(columns='Duration', inplace=True)

min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df_normalized = pd.DataFrame(np_scaled)
d = df_normalized.T
f = Top_two_features(d)
print("Most Important Feature in Economy category are:", features[f[0]], 'and ', features[f[1]])
