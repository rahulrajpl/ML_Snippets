import pandas as pd
gdp_const = pd.read_csv("./output/Economy/gross-domestic-product-gdp-constant-price.csv", nrows=1)
gdp_curr = pd.read_csv("./output/Economy/gross-domestic-product-gdp-current-price.csv", nrows=1)
sw_gdp_const = pd.read_csv("./output/Economy/state-wise-net-domestic-product-ndp-constant-price.csv", nrows=1)
sw_gdp_curr = pd.read_csv("./output/Economy/state-wise-net-domestic-product-ndp-current-price.csv", nrows=1)

# print(gdp_const.shape)
# print(gdp_curr.shape)
# print(sw_gdp_const.shape)
# print(sw_gdp_curr.shape)

sw_gdp_const = sw_gdp_const.rename(columns={'All_India NDP':'All_India'})
sw_gdp_curr = sw_gdp_curr.rename(columns={'All_India NDP':'All_India'})
gdp_const = gdp_const.rename(columns={'All_India GDP':'All_India'})
gdp_curr = gdp_curr.rename(columns={'All_India GDP':'All_India'})

df = pd.concat([gdp_curr,gdp_const,sw_gdp_const,sw_gdp_curr])

df['Description']=['GDP_Const','GDP_Curr','NDP_Const','NDP_curr']
df.drop(columns='Duration',inplace=True)
df.set_index('Description',inplace=True)
df_cat1 = df
print(df.T.corr())

print("Inference:Correlation of Economy")
print("It is seen from the correlation of attributes that the features GDP_Constant and GDP_Current are fully correlated. \
It means they are redundant. Thus we can ignore one of these feature as part of feature reduction.\
    Same is the case with State Wise NDP_Constant and State Wise NDP_Curr")

# Doing for demography Category
csr = pd.read_csv("./datagov/Demography/child-sex-ratio-0-6-years.csv")
dgr = pd.read_csv("./datagov/Demography/decadal-growth-rate.csv")
sr = pd.read_csv("./datagov/Demography/sex-ratio.csv")

df = pd.concat([csr.T,dgr.T,sr.T])
df = df.T
df.drop(columns='Category', inplace=True)
df.set_index('Country/ States/ Union Territories Name', inplace=True)
df= df.astype(float)
df_cat2 = df
print(df.corr())
print("Inference: Correlation of Demography")
print("It is seen from above correlation that none of the features of demography are totally correlated. \
Hence, if at all Feature reduction is to be undertaken, those features which are having value closest to 1 can be taken.")


#Doing for Education folder (Only two files contain 2011-12 data.
ger_he = pd.read_csv("./output/Education/gross-enrolment-ratio-higher-education.csv")
print(ger_he.shape)
ger_he = ger_he.set_index('Year').loc['2011-12']
ger_he = ger_he.reset_index()
ger_he = ger_he.drop(columns='Year')
ger_he = ger_he.set_index('Country/ State/ UT Name')
df_cat3 = ger_he
print(ger_he.corr())

# Doing for Lit rate original file.
lit_rate = pd.read_csv("./datagov/Education/literacy-rate-7-years.csv")
lit_rate.drop(columns='Category',inplace=True)
lit_rate.set_index('Country/ States/ Union Territories Name', inplace=True)
df_cat3_1 = lit_rate
print(lit_rate.corr())
print("Inference:Correlation of Education - literacy rate")
print("It is seen from above correlation that none of the features of Education are totally correlated. \
However, if at all redundancy to be handled, we can drop one of the features where correlation value is \
0.985199 and 0.971140, etc. in that decreasing order\
Hence, if at all Feature reduction is to be undertaken, those features which are having value closest to 1 can be taken.")

# ---------------------------------
# Correlation across categories
col_names = []
list(df_cat2.index)
for i in list(df_cat2.index):
    for j in i:
        col_names.append(j)
        break

df_cat2.index.name = "States"
df_cat2.reset_index(inplace=True)
df_cat2['States'] = col_names
df_cat2 = df_cat2.set_index('States')
df_cat1.rename(columns = {'All_India': 'INDIA'}, inplace=True)
df_cat1 = df_cat1.T
df_cat1.reset_index(inplace=True)
df_cat1.rename(columns={'index':'States'}, inplace=True)
df_cat2.reset_index(inplace=True)
newdf = pd.merge(df_cat1,df_cat2,how='outer',on='States')

df_cat3.reset_index(inplace=True)
df_cat3.head()
df_cat3.rename(columns={'Country/ State/ UT Name':'States'}, inplace=True)
newdf1=pd.merge(newdf, df_cat3, how='outer', on='States')

df_cat3_1.reset_index(inplace=True)
df_cat3_1.rename(columns={'Country/ States/ Union Territories Name':'States'}, inplace=True)
df_cat3_1.reset_index(inplace=True)
newdf2=pd.merge(newdf1, df_cat3_1, how='outer', on='States')
newdf2.corr()
print(newdf2.corr())