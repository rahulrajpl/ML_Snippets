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

gdp_const.drop(columns=['Items Description'], inplace = True)
gdp_const.drop(index=11, inplace=True)
gdp_curr.drop(columns=['Items  Description'], inplace = True, axis=1)
sw_gdp_const.drop(columns=['Item Description'], inplace = True)
sw_gdp_const.drop(index=11, inplace=True)
sw_gdp_curr.drop(columns=['Item Description'], inplace = True)
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
gdp_const.to_csv("./output/Economy/gross-domestic-product-gdp-constant-price.csv")
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
gdp_const.to_csv("./output/Economy/gross-domestic-product-gdp-current-price.csv")
print("GDP_curr cleaned and saved to output folder")
#---------

# Cleaning sw_gdp_const Start
rwise_states = []
for reg in dr.groups.keys():
    states = [i for i in dr.get_group(reg)['States and Union Territories'] if i in sw_gdp_const.columns]
    rwise_states.append(states)
# Calculating the mean of nan region wise.
for rstate in rwise_states:
    sw_gdp_const[rstate] = sw_gdp_const[rstate].apply(lambda row: row.fillna(row.mean()), axis=1)
sw_gdp_const.to_csv("./output/Economy/state-wise-net-domestic-product-ndp-constant-price.csv")
print("sw_gdp_const cleaned and saved to output folder")
#---------

# Cleaning sw_gdp_curr Start
rwise_states = []
for reg in dr.groups.keys():
    states = [i for i in dr.get_group(reg)['States and Union Territories'] if i in sw_gdp_curr.columns]
    rwise_states.append(states)
# Calculating the mean of nan region wise.
for rstate in rwise_states:
    sw_gdp_curr[rstate] = sw_gdp_curr[rstate].apply(lambda row: row.fillna(row.mean()), axis=1)
sw_gdp_curr.fillna(method='ffill', inplace=True)
sw_gdp_curr.to_csv("./output/Economy/state-wise-net-domestic-product-ndp-current-price.csv")
print("sw_gdp_curr cleaned and saved to output folder")
#-----------

# Cleaning ger_he Start
rwise_states = []
ger_he.set_index('Year', inplace=True)
gerIndex = set(list(ger_he.index))
gerdf = []
for gI in gerIndex:
    gerdf.append(ger_he.T[gI].T)

new_gerdf = []
y = {0: '2011', 1: '2012', 2: '2013', 3: '2014', 4: '2015', 5: '2016'}
# y = ['2016', '2011', '2012', '2013', '2014', '2015']

for i in range(len(gerdf)):
    ger_temp = gerdf[i].reset_index()
    ger_temp.drop(columns='Year', inplace=True)
    ger_temp.set_index('Country/ State/ UT Name', inplace=True)
    ger_temp = ger_temp.T
    ger_temp = ger_temp.rename(columns={'Chhatisgarh': 'Chhattisgarh',
                                        'Jammu and Kashmir': 'Jammu & Kashmir',
                                        'Uttrakhand': 'Uttarakhand',
                                        'Dadra & Nagar Haveli': 'D & N Haveli',
                                        'Andaman & Nicobar Islands': 'A & N Islands',
                                        'Delhi': 'NCT of Delhi'
                                        })
    # for col in list(r['States and Union Territories']):
    #     if col not in ger_temp.columns:
    #         ger_temp[col] = 0
    rwise_states = []

    for reg in dr.groups.keys():
        states = [i for i in dr.get_group(reg)['States and Union Territories'] if i in ger_temp.columns]
        rwise_states.append(states)

    for rstate in rwise_states:
        ger_temp[rstate] = ger_temp[rstate].apply(lambda row: row.fillna(row.mean()), axis=1)
    ger_temp = ger_temp.T
    ger_temp['Year'] = y[i]
    new_gerdf.append(ger_temp)
final_gerdf = pd.concat([new_gerdf[1],new_gerdf[2],new_gerdf[3],new_gerdf[4],new_gerdf[5],new_gerdf[0]])
final_gerdf.to_csv("./output/Education/gross-enrolment-ratio-higher-education.csv")
print("ger_he cleaned and saved to output folder")
#-----------


exit()