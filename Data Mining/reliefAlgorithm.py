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
            #             nmiss.append(min(sorted([np.linalg.norm(i-j) for j in d.iloc[x]])[1:]))
            t = [np.linalg.norm(i - j) for j in d.iloc[x]]
            t.sort()
            nmiss.append(min(t[1:]))
        #         print('Length of nmiss', len(nmiss))
        # Finding NearHit value
        for k in d[d.columns[x]]:
            t = [np.linalg.norm(k - l) for l in d[d.columns[x]]]
            t.sort()
            nhit.append(min(t[1:]))
        #         print('Length of nhit', len(nhit))
        #       nhit.append(min(sorted([np.linalg.norm(k-l) for l in d[d.columns[x]]])[1:]))
        # Calculating the scores of the feature
        for i in range(len(d[d.columns[x]])):
            s -= nhit[i] + nmiss[i]
        scores.append(s)
    #     print(scores)
    # Feature with highest score is
    f1 = scores.index(max(sorted(scores)))
    # Feature with second highest score is
    f2 = scores.index(max(sorted(scores)[:-1]))
    return (f1, f2)


def normalise(dataframe):
    df = dataframe
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(df)
    return pd.DataFrame(np_scaled)

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
df = df.T
df_normalized = normalise(df)

d = df_normalized
f = Top_two_features(d)
print("Most Important Feature in Economy category are:", features[f[0]], 'and ', features[f[1]])

# Doing for Demography
csr = pd.read_csv("./datagov/Demography/child-sex-ratio-0-6-years.csv")
dgr = pd.read_csv("./datagov/Demography/decadal-growth-rate.csv")
sr = pd.read_csv("./datagov/Demography/sex-ratio.csv")
for d in [csr,dgr,sr]:
    d.drop(columns='Category', inplace=True)
temp = pd.merge(csr,dgr,how='outer', on='Country/ States/ Union Territories Name')
df = pd.merge(temp,sr, how='outer', on='Country/ States/ Union Territories Name')
features = list(df.columns)[1:]
df.set_index('Country/ States/ Union Territories Name', inplace=True)
df = normalise(df)
f = Top_two_features(df)
print("Most Important Feature in Demography category are:", features[f[0]], 'and ', features[f[1]])

# Doing for Education

