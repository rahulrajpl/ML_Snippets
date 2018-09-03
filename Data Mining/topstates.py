import pandas as pd
import numpy as np
from collections import OrderedDict
from sklearn import preprocessing

gdp_const = pd.read_csv("./output/Economy/gross-domestic-product-gdp-constant-price.csv")
gdp_curr = pd.read_csv("./output/Economy/gross-domestic-product-gdp-current-price.csv")
sw_gdp_const = pd.read_csv("./output/Economy/state-wise-net-domestic-product-ndp-constant-price.csv")
sw_gdp_curr = pd.read_csv("./output/Economy/state-wise-net-domestic-product-ndp-current-price.csv")

gdp_const_2011 = pd.DataFrame(gdp_const.loc[0]).T
gdp_curr_2011 = pd.DataFrame(gdp_curr.loc[0]).T
sw_gdp_const_2011 = pd.DataFrame(sw_gdp_const.loc[0]).T
sw_gdp_const_2011 = sw_gdp_const_2011.T.reset_index()
sw_gdp_const_2011.drop(index=0, inplace=True)
sw_gdp_const_2011=sw_gdp_const_2011.T
sw_gdp_curr_2011 = pd.DataFrame(sw_gdp_curr.loc[0])
sw_gdp_curr_2011 = sw_gdp_curr_2011.reset_index()
sw_gdp_curr_2011.drop(index=0,inplace=True)
sw_gdp_curr_2011 =sw_gdp_curr_2011.T
df1 = pd.concat([gdp_const_2011, gdp_curr_2011])
sw_gdp_const_2011 = sw_gdp_const_2011.T.set_index('index').T
sw_gdp_curr_2011 = sw_gdp_curr_2011.T.set_index('index').T
df2 = pd.concat([sw_gdp_const_2011, sw_gdp_curr_2011])
df2 = df2.T
del df2.index.name
df2 = df2.T
df2 = df2.rename(columns={
    'All_India NDP':'All_India'
})
df1 = df1.rename(columns={
    'All_India GDP':'All_India'
})
df = pd.concat([df1, df2], sort=False)
df.set_index('Duration',inplace=True)
# df = df.drop(columns='Unnamed: 0') # Removing an extra column. This error was not observed in Jupyter Notebook.
# Creating a dictionary with distance as key and corresponding state as value
dist = {}
v2 = df['All_India']
for col in df.columns:
    v1 = df[col]
    dist[np.linalg.norm(v1-v2)]=col

# For ordering the dictionary values as per the keys
dist = OrderedDict(sorted(dist.items()))

# Filtering the top five states from the list ordered dictionary.
top_states = []
keys = list(dist.keys())
for k in keys[1:6]:
    top_states.append(dist[k])

print('Top States of India for Economy are (Without Normalising) : ', top_states)
# result = pd.DataFrame(top_states)
# result.to_csv("./output/Top_FiveStates_Economy.csv", index=False)
# print("File saved to location ./output/Top_FiveStates_Economy.csv")

# Calculating the with Normalised values
df =pd.concat([df1,df2], sort=False)
df['Duration'] = ['gdp-constant-price','gdp-current-price','ndp-constant-price','ndp-current-price']
df = df.set_index('Duration').T
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df_normalized = pd.DataFrame(np_scaled)
df_normalized = df_normalized.T

# Ranking all States and saving in Dictionary as rank, state pair
dist = {}
v0 = df_normalized[df_normalized.columns[33]] # Storing India vector constant
# Looping through all States vectors
for i in df_normalized.columns:
    v1 = df_normalized[df_normalized.columns[i]]
    dist[np.linalg.norm(v1-v0)] = df.T.columns[i]
dist = OrderedDict(sorted(dist.items()))

# Extracting the first five states as per ranking
norm_idx = []
for k in dist.keys():
    norm_idx.append(dist[k])
norm_idx = norm_idx[1:6]

print('Top States of India for Economy are (with Normalising) : ', norm_idx)
# pd.DataFrame(result_normalised).to_csv("./output/Top_FiveStates_Economy_Normalised.csv", index=False)
# print("Top Five States saved to location ./output/Top_FiveStates_Economy_Normalised.csv")
# End of calculations for Economy Category


#-----------------------------------------
# Starting calculations for Demography Category

csr = pd.read_csv("./datagov/Demography/child-sex-ratio-0-6-years.csv")
dgr = pd.read_csv("./datagov/Demography/decadal-growth-rate.csv")
sr = pd.read_csv("./datagov/Demography/sex-ratio.csv")
csr.drop(columns='Category', inplace=True)
dgr.drop(columns='Category', inplace=True)
sr.drop(columns='Category', inplace=True)
csr.set_index('Country/ States/ Union Territories Name', inplace=True)
dgr.set_index('Country/ States/ Union Territories Name', inplace=True)
sr.set_index('Country/ States/ Union Territories Name', inplace=True)

# Concatinated all the data together for calculation
df1 = pd.concat([csr.T,dgr.T,sr.T])
# Without normalising
dist = {}
v2 = df1['INDIA']
for col in df1.columns:
    v1 = df1[col]
    dist[np.linalg.norm(v1-v2)]=col
dist = OrderedDict(sorted(dist.items()))
top_states = []
for k in dist.keys():
    top_states.append(dist[k])
print('Top States of India for Demography are (Without Normalising) : ', top_states[1:6])

# With normalising
df = pd.concat([csr.T,dgr.T,sr.T])
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df_normalized = pd.DataFrame(np_scaled)
# Ranking all States and saving in Dictionary as rank, state pair
dist = {}
v0 = df_normalized[0] # Storing India vector constant
# Looping through all States vectors
for i in df_normalized.columns:
    v1 = df_normalized[i]
    dist[np.linalg.norm(v1-v0)] = df.columns[i]
dist = OrderedDict(sorted(dist.items()))
norm_idx = []
for k in dist.keys():
    norm_idx.append(dist[k])
norm_idx = norm_idx[1:6]
print('Top States of India for Demography are (With Normalising) : ', norm_idx)

# -------------------------
# Staring Education ranking
ger_he = pd.read_csv("./output/Education/gross-enrolment-ratio-higher-education.csv")
ger_he = ger_he.set_index('Year').loc['2011-12']
# print(ger_he.index)
ger_he = ger_he.reset_index()
ger_he = ger_he.drop(columns='Year')
ger_he = ger_he.set_index('Country/ State/ UT Name').T
# ger_he = ger_he.T

# Finding Top states without normalising...
dist = {}
v2 = ger_he['All India']
for col in ger_he.columns:
    v1 = ger_he[col]
    dist[np.linalg.norm(v1-v2)]=col
dist = OrderedDict(sorted(dist.items()))
top_states = []
for k in dist.keys():
    top_states.append(dist[k])
print('Top States of India for Education are (Without Normalising) : ', top_states[1:6])

# Top States in Education with Normalising
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(ger_he)
df_normalized = pd.DataFrame(np_scaled)
# Ranking all States and saving in Dictionary as rank, state pair
dist = {}
v0 = df_normalized[35] # Storing India vector constant
# Looping through all States vectors
for i in df_normalized.columns:
    v1 = df_normalized[i]
    dist[np.linalg.norm(v1-v0)] = ger_he.columns[i]
dist = OrderedDict(sorted(dist.items()))
norm_idx = []
for k in dist.keys():
    norm_idx.append(dist[k])
norm_idx = norm_idx[1:6]
print('Top States of India for Demography are (With Normalising) : ', norm_idx)