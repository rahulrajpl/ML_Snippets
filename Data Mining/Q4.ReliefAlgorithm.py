from sklearn import preprocessing
import pandas as pd
import numpy as np
from collections import OrderedDict

def relief_algorithm(df, rwise_states, Allstates):
    # Implemented as per https://en.wikipedia.org/wiki/Relief_(feature_selection)
    nearest_miss = {}
    nearest_hit = {}
    for g in rwise_states:
        other_region_states = [s for s in Allstates if s not in g]

        for col in df[g].columns:
            # Calculating the near miss
            nmiss = []
            for i in other_region_states:
                nmiss.append(np.linalg.norm(df[col] - df[i]))
            nearest_miss[col] = min(nmiss)
            # Calculating the near hit
            try:
                nhit = []
                for i in df[g].columns:
                    nhit.append(np.linalg.norm(df[col] - df[i]))
                nhit.sort()
                nearest_hit[col] = min(nhit[1:])
            except ValueError:
                nearest_hit[col] = 0
    #     Calculating the scores of each feature vector
    scores = {}
    for f in df.index:
        s = 0
        for state in df.columns[:-1]:
            fs = df.at[f, state]
            s -= (fs - nearest_hit[state]) ** 2 + (fs - nearest_miss[state]) ** 2
        scores[s] = f
    scores = OrderedDict(sorted(scores.items(), reverse=True))
    # print(scores.keys())
    top2features = []
    for feature in list(scores.values())[:2]:
        top2features.append(feature)
    return top2features

def normalise(dataframe):
    min_max_scaler = preprocessing.MinMaxScaler()
    dataframe[dataframe.columns] = min_max_scaler.fit_transform(dataframe[dataframe.columns])
    return pd.DataFrame(dataframe[dataframe.columns])

def df_cleaning(df):
    try:
        df.drop(columns='Region', inplace=True)
    except KeyError:
        pass

    df.set_index('States and Union Territories', inplace=True)

    Allstates = df.index[:-1]
    reg = r.groupby('Region')
    region = list(reg.groups)
    df = df.T
    df = normalise(df)  # Normalising for applying relief algorithm
    rwise_states = []
    for state_reg in region:
        states = []
        for state in df[list(reg.get_group(state_reg)['States and Union Territories'])].columns:
            states.append(state)
        rwise_states.append(states)
    return df, rwise_states, Allstates

# Reading Cleaned data files in each category
df_demog = pd.read_csv('./output/Demography/Demography.csv')
df_economy= pd.read_csv('./output/Economy/Economy.csv')
df_education = pd.read_csv('./output/Education/Education.csv')
r = pd.read_csv("regions.csv")

df_all = pd.merge(df_demog, df_economy, how='outer', on='States and Union Territories')
df_all = pd.merge(df_all, df_education, how='outer', on='States and Union Territories')

# Applying Relief Algorithm for Demography Category
df, rwise_states, Allstates = df_cleaning(df_demog)
f = relief_algorithm(df, rwise_states, Allstates)
print('\nTop Two features in Demography category are  \n1.', f[0], '\n2.', f[1])
d1 = pd.DataFrame(df.loc[f[0]])
d2 = pd.merge(d1, pd.DataFrame(df.loc[f[1]]), how='outer', on='States and Union Territories')
d2.to_csv('./output/Demography/Top2Feature.csv')
print('Dataframe saved to ./output/Demography/Top2Feature.csv')

# Applying Relief Algorithm for Economy Category
df, rwise_states, Allstates = df_cleaning(df_economy)
f = relief_algorithm(df, rwise_states, Allstates)
print('\nTop Two features in Economy category are  \n1.', f[0], '\n2.', f[1])
d1 = pd.DataFrame(df.loc[f[0]])
d2 = pd.merge(d1, pd.DataFrame(df.loc[f[1]]), how='outer', on='States and Union Territories')
d2.to_csv('./output/Economy/Top2Feature.csv')
print('Dataframe saved to ./output/Economy/Top2Feature.csv')

# Applying Relief Algorithm for Education Category
df, rwise_states, Allstates = df_cleaning(df_education)
f = relief_algorithm(df, rwise_states, Allstates)
print('\nTop Two features in Education category are  \n1.', f[0], '\n2.', f[1])
d1 = pd.DataFrame(df.loc[f[0]])
d2 = pd.merge(d1, pd.DataFrame(df.loc[f[1]]), how='outer', on='States and Union Territories')
d2.to_csv('./output/Education/Top2Feature.csv')
print('Dataframe saved to ./output/Education/Top2Feature.csv')

# Applying Relief Algorithm across category
df, rwise_states, Allstates = df_cleaning(df_all)
f = relief_algorithm(df, rwise_states, Allstates)
print('\nTop Two features across category are  \n1.', f[0], '\n2.', f[1])
d1 = pd.DataFrame(df.loc[f[0]])
d2 = pd.merge(d1, pd.DataFrame(df.loc[f[1]]), how='outer', on='States and Union Territories')
d2.to_csv('./output/Top2Feature_AllIndia.csv')
print('Dataframe saved to ./output/Top2Feature_AllIndia.csv')