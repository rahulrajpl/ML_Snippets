import pandas as pd
import numpy as np
r = pd.read_csv("regions.csv")

def merge_demography():
    df_demo1 = pd.read_csv('./datagov/Demography/child-sex-ratio-0-6-years.csv')
    df_demo2 = pd.read_csv('./datagov/Demography/decadal-growth-rate.csv')
    df_demo3 = pd.read_csv('./datagov/Demography/sex-ratio.csv')
    df_demo = pd.merge(df_demo1, df_demo2, how='outer', on='Country/ States/ Union Territories Name')
    df_demo = pd.merge(df_demo, df_demo3, how='outer', on='Country/ States/ Union Territories Name')
    df_demo.drop(columns=['Category_x', 'Category_y', 'Category'], inplace=True)
    df_demo.rename(columns={
        'Country/ States/ Union Territories Name': 'States and Union Territories'
    }, inplace=True)
    df_demo = pd.merge(r, df_demo, how='outer', on='States and Union Territories')
    df_demo.to_csv('./output/Demography/Demography.csv', index=None)
    print('Merged Demography data saved to ./output/Demography/Demography.csv. Shape is', df_demo.shape)

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
    print('Merged Economy data saved to /output/Economy/Economy.csvShape is', df_economy.shape)

def merge_education():

    def cleandor():
        # Cleaning Drop out Rate file
        dor = pd.read_csv("./datagov/Education/drop-out-rate.csv")
        dor.set_index('State_UT', inplace=True)
        dor.replace('NR', 0, inplace=True)
        dor.iloc[0:1, 4:5] = dor.iloc[1:2, 4:5]
        dor[dor.columns[2:]] = dor[dor.columns[2:]].apply(pd.to_numeric)
        dor.rename(index={'All India': 'INDIA', 'Arunachal  Pradesh': 'Arunachal Pradesh',
                          'Dadra & Nagar Haveli': 'D & N Haveli', 'Madhya  Pradesh': 'Madhya Pradesh',
                          'Delhi': 'NCT of Delhi', 'Tamil  Nadu': 'Tamil Nadu'}, inplace=True)
        dor.reset_index(inplace=True)
        dor = dor.pivot(index='State_UT', columns='year')
        dor.columns = [' '.join(col).strip() for col in dor.columns.values]
        dor.reset_index(inplace=True)
        dor.rename(columns={'State_UT': 'States and Union Territories'}, inplace=True)
        dor = pd.merge(r, dor, how='outer', on='States and Union Territories')
        # print(dor)

    def cleanger_he():
        # Cleaning Gross Enrollment Rate _High Education file.
        ger_he = pd.read_csv("./datagov/Education/gross-enrolment-ratio-higher-education.csv")

        ger_he.rename(columns={'Country/ State/ UT Name': 'States and Union Territories'}, inplace=True)
        ger_he.set_index('States and Union Territories', inplace=True)
        ger_he.rename(index={'Chhatisgarh': 'Chhattisgarh','Jammu and Kashmir': 'Jammu & Kashmir',
                             'Uttrakhand': 'Uttarakhand','Dadra & Nagar Haveli': 'D & N Haveli',
                             'Andaman & Nicobar Islands': 'A & N Islands','Delhi': 'NCT of Delhi',
                             'All India': 'INDIA'}, inplace=True)
        ger_he.reset_index(inplace=True)
        ger_he = ger_he.pivot(index='States and Union Territories', columns='Year')
        ger_he.columns = [' '.join(col).strip() for col in ger_he.columns.values]
        ger_he = pd.merge(r, ger_he, how='outer', on='States and Union Territories')
        # print(ger_he.columns)

    def cleanger_schools():
        # Cleaning Gross Enrollment Rate School file.
        ger_schools = pd.read_csv("./datagov/Education/gross-enrolment-ratio-schools.csv")
        ger_schools.rename(columns={'State_UT': 'States and Union Territories'}, inplace=True)
        ger_schools.set_index('States and Union Territories', inplace=True)
        ger_schools.rename(index={'Chhatisgarh': 'Chhattisgarh', 'Jammu And Kashmir': 'Jammu & Kashmir',
                                  'Uttrakhand': 'Uttarakhand', 'Dadra & Nagar Haveli': 'D & N Haveli',
                                  'Andaman & Nicobar Islands': 'A & N Islands', 'Delhi': 'NCT of Delhi',
                                  'All India': 'INDIA', 'Uttaranchal': 'Uttarakhand',
                                  'Pondicherry': 'Puducherry', 'MADHYA PRADESH': 'Madhya Pradesh'}, inplace=True)
        ger_schools.reset_index(inplace=True)
        ger_schools = ger_schools.pivot(index='States and Union Territories', columns='Year')
        ger_schools.columns = [' '.join(col).strip() for col in ger_schools.columns.values]
        # print(ger_schools)

    def cleanlit():
        lit_rate = pd.read_csv("./datagov/Education/literacy-rate-7-years.csv")
        lit_rate.drop(columns='Category', inplace=True)
        lit_rate.rename(columns={"Country/ States/ Union Territories Name": "States and Union Territories"},
                        inplace=True)
        lit_rate = pd.merge(r, lit_rate, how='outer', on='States and Union Territories')
        print(lit_rate)

    def cleanper_boys_toilet():
        per_boys_toilet = pd.read_csv("./datagov/Education/percentage-schools-boys-toilet.csv")
        per_boys_toilet.rename(columns={'State_UT': 'States and Union Territories'}, inplace=True)
        per_boys_toilet.set_index('States and Union Territories', inplace=True)
        per_boys_toilet.reset_index(inplace=True)
        per_boys_toilet = per_boys_toilet.pivot(index='States and Union Territories', columns='year')
        per_boys_toilet.columns = [' '.join(col).strip() for col in per_boys_toilet.columns.values]
        # per_boys_toilet.reset_index(inplace=True)
        per_boys_toilet.rename(
            index={'Jammu And Kashmir': 'Jammu & Kashmir', 'Andaman & Nicobar Islands': 'A & N Islands',
                   'Dadra & Nagar Haveli': 'D & N Haveli', 'Delhi': 'NCT of Delhi',
                   'All India': 'INDIA'}, inplace=True)
        per_boys_toilet = pd.merge(r, per_boys_toilet, how='outer', on='States and Union Territories')
        # print(per_boys_toilet)

    def cleanper_girls_toilet():
        per_girls_toilet = pd.read_csv("./datagov/Education/percentage-schools-girls-toilet.csv")
        per_girls_toilet.rename(columns={'State_UT': 'States and Union Territories'}, inplace=True)
        per_girls_toilet = per_girls_toilet.pivot(index='States and Union Territories', columns='year')
        per_girls_toilet.columns = [' '.join(col).strip() for col in per_girls_toilet.columns.values]
        per_girls_toilet.rename(
            index={'Jammu And Kashmir': 'Jammu & Kashmir', 'Andaman & Nicobar Islands': 'A & N Islands',
                   'Dadra & Nagar Haveli': 'D & N Haveli', 'Delhi': 'NCT of Delhi',
                   'All India': 'INDIA'}, inplace=True)
        per_girls_toilet = pd.merge(r, per_girls_toilet, how='outer', on='States and Union Territories')
        # print(per_girls_toilet)

    def cleanper_comps():
        per_comps = pd.read_csv("./datagov/Education/percentage-schools-computers.csv")
        per_comps.rename(columns={'State_UT': 'States and Union Territories'}, inplace=True)
        per_comps = per_comps.pivot(index='States and Union Territories', columns='year')
        per_comps.columns = [' '.join(col).strip() for col in per_comps.columns.values]
        per_comps.rename(
            index={'Jammu And Kashmir': 'Jammu & Kashmir', 'Andaman & Nicobar Islands': 'A & N Islands',
                   'Dadra & Nagar Haveli': 'D & N Haveli', 'Delhi': 'NCT of Delhi',
                   'All India': 'INDIA'}, inplace=True)
        per_comps = pd.merge(r, per_comps, how='outer', on='States and Union Territories')
        print(per_comps)

    def cleanper_drinking():
        per_drinking = pd.read_csv("./datagov/Education/percentage-schools-drinking-water.csv")
        per_electricity = pd.read_csv("./datagov/Education/percentage-schools-electricity.csv")
        per_electricity.rename(columns={'State_UT': 'States and Union Territories'}, inplace=True)



    # cleandor()
    # cleanger_he()
    # cleanger_schools()
    # cleanlit()
    # cleanper_boys_toilet()
    # cleanper_girls_toilet()
    # cleanper_comps()
    cleanper_drinking()
def main():
   # merge_demography()
   # merge_economy()
   merge_education()

if __name__== '__main__':
    main()
