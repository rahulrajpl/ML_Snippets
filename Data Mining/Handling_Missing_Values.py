import pandas as pd
import numpy as np

r = pd.read_csv("regions.csv")
# csr = pd.read_csv("./datagov/Demography/child-sex-ratio-0-6-years.csv")
# dgr = pd.read_csv("./datagov/Demography/decadal-growth-rate.csv")
# sr = pd.read_csv("./datagov/Demography/sex-ratio.csv")
gdp_const = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-constant-price.csv")
gdp_curr = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-current-price.csv")
sw_gdp_const = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-constant-price.csv")
# sw_gdp_curr = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-current-price.csv")
# dor = pd.read_csv("./datagov/Education/drop-out-rate.csv")
# ger_he = pd.read_csv("./datagov/Education/gross-enrolment-ratio-higher-education.csv")
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

# Correcting State names
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
rwise = r.groupby('Region')['States and Union Territories'].apply(list).to_dict()
# Grouping the States in the GDP Dataframe
rwise_states = []
dr = r.groupby('Region')
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




exit()