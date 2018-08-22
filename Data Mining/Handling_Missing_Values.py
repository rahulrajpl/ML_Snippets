import csv
with open("regions.csv", 'r', encoding='latin-1') as f:
    regions = list(csv.reader(f))
with open("./Data\ Mining/datagov/Demography/child-sex-ratio-0-6-years.csv", 'r', encoding='latin-1') as f:
    child_sex_ration = list(csv.reader(f))

region = [r[1] for r in regions[1:]]
print(len(set(region)))
