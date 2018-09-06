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
df1 = df.copy()
df.drop(columns='Duration', inplace=True)
df.drop(columns='Items Description', inplace=True)
df = df.T
df_normalized = normalise(df)
f = Top_two_features(df_normalized)
print('Top 2 features in Economy category are:\n\t', features[f[0]], '\n\t', features[f[1]])

# Doing for Demography
csr = pd.read_csv("./datagov/Demography/child-sex-ratio-0-6-years.csv")
dgr = pd.read_csv("./datagov/Demography/decadal-growth-rate.csv")
sr = pd.read_csv("./datagov/Demography/sex-ratio.csv")
for d in [csr,dgr,sr]:
    d.drop(columns='Category', inplace=True)
temp = pd.merge(csr,dgr,how='outer', on='Country/ States/ Union Territories Name')
df = pd.merge(temp,sr, how='outer', on='Country/ States/ Union Territories Name')
df2 = df.copy()
features = list(df.columns)[1:]
df.set_index('Country/ States/ Union Territories Name', inplace=True)
df2 = df
df = normalise(df)
f = Top_two_features(df)
print('Top 2 features in Demography category are:\n\t', features[f[0]], '\n\t', features[f[1]])

# Doing for Education
ger_he = pd.read_csv("./output/Education/gross-enrolment-ratio-higher-education.csv")
ger_he.set_index('index', inplace=True)
ger_he = ger_he.T
features = list(ger_he.columns)
df3 = ger_he.copy()
df = normalise(ger_he)
f = Top_two_features(df)
print('Top 2 features in Gross Enrollment Ratio are:\n\t', features[f[0]], '\n\t', features[f[1]])

# For Litaracy rate (2011 data only 2 columns)
lit_rate = pd.read_csv("./datagov/Education/literacy-rate-7-years.csv")
lit_rate.drop(columns='Category', inplace=True)
lit_rate.set_index('Country/ States/ Union Territories Name', inplace=True)
lit_rate = lit_rate[['Literacy rate (Persons) - Total - 2011',\
                    'Literacy rate (Persons) - Rural - 2011',\
                    'Literacy rate (Persons) - Urban - 2011']]
features = list(lit_rate.columns)
df4 = lit_rate.copy()
df = normalise(lit_rate)
f = Top_two_features(df)
print('Top 2 features in Litaracy rate are:\n\t', features[f[0]], '\n\t', features[f[1]])

# ------------------------
# Finding best two across category
# print(df1)
# df1 = df1.T
df1.set_index('Items Description',inplace=True)
# df1 = df1.T
# print(df2.columns)

# df2.set_index('Country/ States/ Union Territories Name', inplace=True)
df1.index.name = 'Country/ States/ Union Territories Name'
df12 =pd.merge(df1, df2, how='outer', on='Country/ States/ Union Territories Name')
# df12 = df12.T
df12.drop(columns="Duration",inplace=True)
# df12=df12.T
df3.index.name = 'Country/ States/ Union Territories Name'
df123 = pd.merge(df12, df3, how='outer', on='Country/ States/ Union Territories Name')
df3.reset_index(inplace=True)
df1234 = pd.merge(df123, df4, how='outer', on='Country/ States/ Union Territories Name')
print(df1234)