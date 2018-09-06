import pandas as pd
import numpy as np
r = pd.read_csv("regions.csv")

def merge_demography():
    # Merging Demography
    df_demo1 = pd.read_csv('./datagov/Demography/child-sex-ratio-0-6-years.csv')
    df_demo2 = pd.read_csv('./datagov/Demography/decadal-growth-rate.csv')
    df_demo3 = pd.read_csv('./datagov/Demography/sex-ratio.csv')
    df_demo = pd.merge(df_demo1, df_demo2, how='outer', on='Country/ States/ Union Territories Name')
    df_demo = pd.merge(df_demo, df_demo3, how='outer', on='Country/ States/ Union Territories Name')
    df_demo.drop(columns=['Category_x', 'Category_y', 'Category'], inplace=True)
    df_demo.rename(columns={
        'Country/ States/ Union Territories Name': 'States and Union Territories'
    }, inplace=True)
    df_demo = pd.merge(df_demo, pd.DataFrame(r['States and Union Territories']), \
                       how='outer', on='States and Union Territories')
    df_demo.to_csv('./output/Demography/Demography.csv', index=None)
    print('Merged Demography data saved to ./output/Demography/Demography.csv')

def merge_economy():
    gdp_const = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-constant-price.csv", nrows=11)
    gdp_curr = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-current-price.csv")
    sw_gdp_const = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-constant-price.csv", nrows=11)
    sw_gdp_curr = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-current-price.csv", nrows=11)
    df_in_economy = [gdp_const, gdp_curr, sw_gdp_const, sw_gdp_curr]
    for df in df_in_economy:
        df.rename(columns={'Andhra Pradesh ': 'Andhra Pradesh','West Bengal1': 'West Bengal',
                           'Andaman & Nicobar Islands': 'A & N Islands','Delhi': 'NCT of Delhi',
                           'All_India GDP': 'INDIA','All_India NDP': 'INDIA',
                            'Item Description': 'Item','Items Description': 'Item',
                            'Items  Description': 'Item'}, inplace=True)
    for df in df_in_economy:
        col1 = list(df['Item'])
        col2 = list(df['Duration'])
        cols = [i + j for i, j in zip(col1, col2)]
        df['Items'] = cols
        df.set_index('Items', inplace=True)
        df.drop(columns=['Item', 'Duration'], inplace=True)
        df.columns.name = 'States'
        # print(df.head())
    gdp_const = gdp_const.T
    gdp_curr = gdp_curr.T
    sw_gdp_const = sw_gdp_const.T
    sw_gdp_curr = sw_gdp_curr.T
    df_economy = pd.merge(gdp_const, gdp_curr, how='outer', on='States')
    df_economy = pd.merge(df_economy, sw_gdp_const, how='outer', on='States')
    df_economy = pd.merge(df_economy, sw_gdp_curr, how='outer', on='States')
    df_economy.reset_index(inplace=True)
    df_economy.rename(columns={
        'States': 'States and Union Territories'
    }, inplace=True)
    df_economy = pd.merge(df_economy, pd.DataFrame(r['States and Union Territories']), \
                          how='outer', on='States and Union Territories')

    df_economy.to_csv('./output/Economy/Economy.csv', index=None)
    print('Merged Economy data saved to /output/Economy/Economy.csv')

def merge_education():


def main():
   merge_demography()
   merge_economy()
   merge_education()

if __name__== '__main__':
    main()
