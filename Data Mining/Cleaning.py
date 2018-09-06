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
    # Merging Economy

    # Merging Education


def main():
    merge_category_wise()

if __name__== '__main__':
    main()
