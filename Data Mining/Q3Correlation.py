import pandas as pd
import numpy as np

# Reading Cleaned data files in each category
df_demo = pd.read_csv('./output/Demography/Demography.csv')
df_economy= pd.read_csv('./output/Economy/Economy.csv')
df_education = pd.read_csv('./output/Education/Education.csv')

df_demo[df_demo.columns[2:]].corr().to_csv('./output/Demography/correlation.csv')
print('Correlation of Demography Category is saved to ./output/Demography/correlation.csv')
df_economy[df_economy.columns[1:]].corr().to_csv('./output/Economy/correlation.csv')
print('Correlation of Economy Category is saved to ./output/Economy/correlation.csv')
df_education[df_education.columns[1:]].corr().to_csv('./output/Education/correlation.csv')
print('Correlation of Education Category is saved to ./output/Education/correlation.csv')

df = pd.merge(df_demo, df_economy, how='outer',on='States and Union Territories')
df = pd.merge(df, df_education, how='outer',on='States and Union Territories')
df[df.columns[2:]].corr().to_csv('./output/AllIndia_correlation.csv')
print('Correlation across three categories is saved to ./output/AllIndia_correlation.csv')


print("Inference:")
print("It is seen from above correlations that the features which are having correlation value close to 1 or -1 are\
    redundant. Thus we can ignore one of these feature as part of feature reduction.")
