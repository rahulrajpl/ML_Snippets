import pandas as pd
import numpy as np
from collections import OrderedDict
from sklearn import preprocessing

# Formatting the dataframes for processing Top Five States.
df_demo = pd.read_csv('./output/Demography/Demography.csv')
df_economy= pd.read_csv('./output/Economy/Economy.csv')
df_education = pd.read_csv('./output/Education/Education.csv')
df_demo.drop(columns='Region', inplace =True)
df_demo = df_demo.set_index('States and Union Territories').T
df_economy = df_economy.set_index('States and Union Territories').T
df_education = df_education.set_index('States and Union Territories').T
# End
def FindTopFive(df):

    # Top Five (Without Normalizing)
    states = df.columns[:-1]
    I = df['INDIA']
    dist = {}  # Storing State ranks as a dictionary
    for state in states:
        V = df[state]
        dist[np.linalg.norm(V - I)] = state
    dist = OrderedDict(sorted(dist.items()))
    top_states = []
    keys = list(dist.keys())
    for k in keys[1:6]:
        top_states.append(dist[k])
    return top_states

def FindTopFive_Normalized(df):
    # Top Five (With Normalizing)
    states = df.columns[:-1]
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(df)
    df_norm = pd.DataFrame(np_scaled)
    I = df_norm[df_norm.columns[36]]  # Storing India Vector
    dist = {}
    for i in df_norm.columns[:-1]:
        v1 = df_norm[df_norm.columns[i]]
        dist[np.linalg.norm(I - v1)] = states[i]
    dist = OrderedDict(sorted(dist.items()))
    top_states = []
    keys = list(dist.keys())
    for k in keys[1:6]:
        top_states.append(dist[k])
    return top_states

if __name__ == '__main__':

    print('Top five States(With Normalizing) in Demography category are', FindTopFive(df_demo))
    print('Top five States(With Normalizing) in Demography category are', FindTopFive_Normalized(df_demo))

    print('Top five States(With Normalizing) in Economy category are', FindTopFive(df_economy))
    print('Top five States(With Normalizing) in Economy category are', FindTopFive_Normalized(df_economy))

    print('Top five States(With Normalizing) in Education category are', FindTopFive(df_education))
    print('Top five States(With Normalizing) in Education category are', FindTopFive_Normalized(df_education))

