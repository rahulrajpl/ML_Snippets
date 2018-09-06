import pandas as pd
import numpy as np

def merge_category_wise():
    # Merging Demography
    df_demo1 = pd.read_csv('./datagov/Demography/child-sex-ratio-0-6-years.csv')
    df_demo2 = pd.read_csv('./datagov/Demography/decadal-growth-rate.csv')
    df_demo3 = pd.read_csv('./datagov/Demography/sex-ratio.csv')
    df_demo = pd.merge(df_demo1, df_demo2, how='outer', on='Country/ States/ Union Territories Name')
    df_demo = pd.merge(df_demo, df_demo3, how='outer', on='Country/ States/ Union Territories Name')
    df_demo.drop(columns=['Category_x', 'Category_y', 'Category'], inplace=True)
    df_demo.to_csv('./output/Demography/Demography.csv', index=None)
    # df = pd.read_csv('./output/Demography/Demography.csv')
    # print(df.head())
    # ---------------
    # Merging Economy
    gdp_const = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-constant-price.csv")
    gdp_curr = pd.read_csv("./datagov/Economy/gross-domestic-product-gdp-current-price.csv")
    sw_gdp_const = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-constant-price.csv")
    sw_gdp_curr = pd.read_csv("./datagov/Economy/state-wise-net-domestic-product-ndp-current-price.csv")
    df_in_economy = [gdp_const, gdp_curr, sw_gdp_const, sw_gdp_curr]
    for df in df_in_economy:
        df.rename(columns={'Andhra Pradesh ': 'Andhra Pradesh',
                           'West Bengal1': 'West Bengal',
                           'Andaman & Nicobar Islands': 'A & N Islands',
                           'Delhi': 'NCT of Delhi',
                           'All_India GDP': 'INDIA',
                           'All_India NDP': 'INDIA',
                            'Item Description': 'Item',
                            'Items Description': 'Item',
                            'Items  Description': 'Item'
                           }, inplace=True)
    for df in df_in_economy:
        col1 = list(df['Item'])
        col2 = list(df['Duration'])
        cols = [i + j for i, j in zip(col1, col2)]
        df['Items'] = cols
        df.set_index('Items', inplace=True)
        df.drop(columns=['Item', 'Duration'], inplace=True)
        # print(df.head())
    # Merging Education


def main():
    merge_category_wise()

if __name__== '__main__':
    main()
