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

dist = {}
v2 = df['All_India']
for col in df.columns:
    v1 = df[col]
    dist[np.linalg.norm(v1-v2)]=col
dist = OrderedDict(sorted(dist.items()))

top_states = []
for k in dist.keys():
    top_states.append(k)

print('Top States of India are (Without Normalising) : ', [dist[t] for t in top_states[2:7]])
result = pd.DataFrame([dist[t] for t in top_states[2:7]])
result.index += 1
result.to_csv("./output/Top_FiveStates.csv")
print("Top Five States saved to location ./output/Top_FiveStates.csv")

# Calculating the Normalised version
df = pd.concat([df1,df2], sort=False)
df.to_csv('temp.csv')
df = pd.read_csv('temp.csv')
# print(df.columns)
df.drop(columns=['Unnamed: 0.1'], inplace=True)
# print(df.columns)
df['Duration'] = ['gdp-constant-price','gdp-current-price','ndp-constant-price','ndp-current-price']
df = df.set_index('Duration').T
# print(df[['gdp-current-price', 'ndp-constant-price','ndp-current-price']].T)
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df_normalized = pd.DataFrame(np_scaled)
norm_values = list(df_normalized.T.loc[0])
norm_idx = []
for idx in sorted(norm_values)[-7:]:
    norm_idx.append(norm_values.index(idx))
df = df.reset_index()
result_normalised = [df.loc[i]['index'] for i in norm_idx[1:-1]][::-1]
print('Top States of India are (With Normalising) : ', result_normalised)
pd.DataFrame(result_normalised).to_csv("./output/Top_FiveStates_normalised.csv")
print("Top Five States saved to location ./output/Top_FiveStates_normalised.csv")