import pandas as pd
import numpy as np

r = pd.read_csv("regions.csv")
# csr = pd.read_csv("./datagov/Demography/child-sex-ratio-0-6-years.csv")
# dgr = pd.read_csv("./datagov/Demography/decadal-growth-rate.csv")
# sr = pd.read_csv("./datagov/Demography/sex-ratio.csv")
gdp_const = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-constant-price.csv")
gdp_curr = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-current-price.csv")
sw_gdp_const = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-constant-price.csv")
sw_gdp_curr = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-current-price.csv")
# dor = pd.read_csv("./datagov/Education/drop-out-rate.csv")
ger_he = pd.read_csv("./datagov/Education/gross-enrolment-ratio-higher-education.csv")
# ger_schools = pd.read_csv("./datagov/Education/gross-enrolment-ratio-schools.csv")
# lit_rate = pd.read_csv("./datagov/Education/literacy-rate-7-years.csv")
# per_boys_toilet = pd.read_csv("./datagov/Education/percentage-schools-boys-toilet.csv")
# per_girls_toilet = pd.read_csv("./datagov/Education/percentage-schools-girls-toilet.csv")
# per_comps = pd.read_csv("./datagov/Education/percentage-schools-computers.csv")
# per_drinking = pd.read_csv("./datagov/Education/percentage-schools-drinking-water.csv")
# per_electricity = pd.read_csv("./datagov/Education/percentage-schools-electricity.csv")
features = list(gdp_const['Items Description'])[:-1]
gdp_const.drop(columns=['Items Description'], inplace = True)
gdp_const.drop(index=11, inplace=True)
gdp_curr.drop(columns=['Items  Description'], inplace = True, axis=1)

sw_gdp_const.drop(index=11, inplace=True)

sw_gdp_curr.drop(index=11, inplace=True)

# Correcting State names in dataframes
gdp_const = gdp_const.rename(columns={'Andhra Pradesh ': 'Andhra Pradesh',
                        'West Bengal1': 'West Bengal',
                       'Andaman & Nicobar Islands': 'A & N Islands',
                       'Delhi': 'NCT of Delhi'
                       })
gdp_curr = gdp_curr.rename(columns={'Andhra Pradesh ': 'Andhra Pradesh',
                        'West Bengal1': 'West Bengal',
                       'Andaman & Nicobar Islands': 'A & N Islands',
                       'Delhi': 'NCT of Delhi'
                       })
sw_gdp_const =sw_gdp_const.rename(columns={'Andhra Pradesh ': 'Andhra Pradesh',
                        'West Bengal1': 'West Bengal',
                       'Andaman & Nicobar Islands': 'A & N Islands',
                       'Delhi': 'NCT of Delhi'
                       })
sw_gdp_curr =sw_gdp_curr.rename(columns={'Andhra Pradesh ': 'Andhra Pradesh',
                        'West Bengal1': 'West Bengal',
                       'Andaman & Nicobar Islands': 'A & N Islands',
                       'Delhi': 'NCT of Delhi'
                       })

dr = r.groupby('Region')

# Grouping the States in the GDP Dataframe
rwise_states = []
for reg in dr.groups.keys():
    states = [i for i in dr.get_group(reg)['States and Union Territories'] if i in gdp_const.columns]
    rwise_states.append(states)
# Calculating the mean of nan region wise.
for rstate in rwise_states:
    gdp_const[rstate] = gdp_const[rstate].apply(lambda row: row.fillna(row.mean()), axis=1)
# Those regional states where all values are NaN. Mean cannot be taken. So used ffill used.
# Last year's data of same state being filled as an estimate.
gdp_const.fillna(method='ffill', inplace=True)
# Saving final cleaned file to output folder
gdp_const.rename(columns={'All_India GDP':'INDIA'},inplace=True)
gdp_const['Items Description'] = features
gdp_const.to_csv("./output/Economy/gross-domestic-product-gdp-constant-price.csv", index=False)
print("GDP_const cleaned and saved to output folder")

#---------
#Cleaning gdp_curr Start
rwise_states = []
for reg in dr.groups.keys():
    states = [i for i in dr.get_group(reg)['States and Union Territories'] if i in gdp_curr.columns]
    rwise_states.append(states)
# Calculating the mean of nan region wise.
for rstate in rwise_states:
    gdp_curr[rstate] = gdp_curr[rstate].apply(lambda row: row.fillna(row.mean()), axis=1)
# Those regional states where all values are NaN. Mean cannot be taken. So used ffill used.
# Last year's data of same state being filled as an estimate.
gdp_curr.fillna(method='ffill', inplace=True)
gdp_curr.rename(columns={'All_India GDP':'INDIA'},inplace=True)
gdp_curr['Items Description'] = features
gdp_curr.to_csv("./output/Economy/gross-domestic-product-gdp-current-price.csv", index=False)
print("GDP_curr cleaned and saved to output folder")
#---------

# Cleaning sw_gdp_const Start
rwise_states = []
features = list(sw_gdp_const['Item Description'])
sw_gdp_const.drop(columns=['Item Description'], inplace = True)
for reg in dr.groups.keys():
    states = [i for i in dr.get_group(reg)['States and Union Territories'] if i in sw_gdp_const.columns]
    rwise_states.append(states)
# Calculating the mean of nan region wise.
for rstate in rwise_states:
    sw_gdp_const[rstate] = sw_gdp_const[rstate].apply(lambda row: row.fillna(row.mean()), axis=1)

sw_gdp_const['Items Description'] = features
sw_gdp_const.rename(columns={'All_India NDP':'INDIA'},inplace=True)
sw_gdp_const.to_csv("./output/Economy/state-wise-net-domestic-product-ndp-constant-price.csv", index=False)
print("sw_gdp_const cleaned and saved to output folder")
#---------

# Cleaning sw_gdp_curr Start
rwise_states = []
features = sw_gdp_curr['Item Description']
sw_gdp_curr.drop(columns=['Item Description'], inplace = True)
for reg in dr.groups.keys():
    states = [i for i in dr.get_group(reg)['States and Union Territories'] if i in sw_gdp_curr.columns]
    rwise_states.append(states)
# Calculating the mean of nan region wise.
for rstate in rwise_states:
    sw_gdp_curr[rstate] = sw_gdp_curr[rstate].apply(lambda row: row.fillna(row.mean()), axis=1)
sw_gdp_curr.fillna(method='ffill', inplace=True)
sw_gdp_curr.rename(columns={'All_India NDP':'INDIA'},inplace=True)

sw_gdp_curr.to_csv("./output/Economy/state-wise-net-domestic-product-ndp-current-price.csv", index=False)
print("sw_gdp_curr cleaned and saved to output folder")
#-----------

# Cleaning ger_he Start (Only for 2011 data)
ger_he.set_index('Year', inplace=True)
ger_he = ger_he.T['2011-12'].T
ger_he.set_index('Country/ State/ UT Name',inplace=True)
ger_he = ger_he.T
ger_he = ger_he.rename(columns={'Chhatisgarh': 'Chhattisgarh',
                                        'Jammu and Kashmir': 'Jammu & Kashmir',
                                        'Uttrakhand': 'Uttarakhand',
                                        'Dadra & Nagar Haveli': 'D & N Haveli',
                                        'Andaman & Nicobar Islands': 'A & N Islands',
                                        'Delhi': 'NCT of Delhi'
                                        })

rwise_states = []
for reg in dr.groups.keys():
    states = [i for i in dr.get_group(reg)['States and Union Territories'] if i in ger_he.columns]
    rwise_states.append(states)
for rstate in rwise_states:
    ger_he[rstate] = ger_he[rstate].apply(lambda row: row.fillna(row.mean()), axis=1)

ger_he.rename(columns={'All India':'INDIA'}, inplace=True)
ger_he.reset_index(inplace=True)
ger_he.to_csv("./output/Education/gross-enrolment-ratio-higher-education.csv", index = False)
print("ger_he cleaned and saved to output folder")
#-----------


exit()