from sklearn import preprocessing
import pandas as pd
import numpy as np

# Reading Cleaned data files in each category
df_demo = pd.read_csv('./output/Demography/Demography.csv')
df_economy= pd.read_csv('./output/Economy/Economy.csv')
df_education = pd.read_csv('./output/Education/Education.csv')


def Top_two_features(dataframe):
    # Normalising
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(dataframe)
    d = pd.DataFrame(np_scaled)
    scores = []

    for x in range(len(d.columns)):
        nmiss = []  # For storing near miss value
        nhit = []  # For storing near hit value
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
    #     fname1 = list(d[d.columns[2:]])[f1]
    #     fname2 = list(d[d.columns[2:]])[f2]
    return (f1, f2)

def normalise(dataframe):
    df = dataframe
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(df)
    return pd.DataFrame(np_scaled)

# Extracting top2 features of Demography category
df_demo.drop(columns='Region', inplace=True)
df_demo.set_index('States and Union Territories',inplace=True)
features = df_demo.columns
df_normalized = normalise(df_demo)
f = Top_two_features(df_normalized)
print('Top 2 features in Demography category are:\n\t', features[f[0]], '\n\t', features[f[1]])
df_demo[[features[f[0]], features[f[1]]]].to_csv('./output/Demography/Top2Feature.csv')
print('Top2Features in Demography category saved as dataframe to folder ./output/Demography/Top2Feature.csv')

# Extracting top2 features of Economy category
features = list(df_economy.columns[1:])
df_economy.set_index('States and Union Territories',inplace=True)
df_normalized = normalise(df_economy)
f = Top_two_features(df_normalized.T)
print('Top 2 features in Economy category are:\n\t', features[f[0]], '\n\t', features[f[1]])
df_economy[[features[f[0]], features[f[1]]]].to_csv('./output/Economy/Top2Feature.csv')
print('Top2Features in Economy category saved as dataframe to folder ./output/Economy/Top2Feature.csv')

# Extracting top2 features of Education category
features = list(df_education.columns[1:])
df_education.set_index('States and Union Territories',inplace=True)
df_normalized = normalise(df_education)
print('This may take a while...please wait...')
f = Top_two_features(df_normalized.T)
print('Top 2 features in Education category are:\n\t', features[f[0]], '\n\t', features[f[1]])
df_education[[features[f[0]], features[f[1]]]].to_csv('./output/Education/Top2Feature.csv')
print('Top2Features in Eduction category saved as dataframe to folder ./output/Education/Top2Feature.csv')

# Extracting top2 features across all three categories
df = pd.merge(df_demo, df_economy, how='outer',on='States and Union Territories')
df = pd.merge(df, df_education, how='outer',on='States and Union Territories')
df_normalized = normalise(df)
print('This may take a while...please wait')
f = Top_two_features(df_normalized.T)
print('Top 2 features across category are:\n\t', features[f[0]], '\n\t', features[f[1]])
df[[features[f[0]], features[f[1]]]].to_csv('./output/Top2Feature_AllIndia.csv')
print('Top2Features across categories saved as dataframe to folder ./output/Top2Feature_AllIndia.csv')
