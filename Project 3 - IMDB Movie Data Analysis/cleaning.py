from pandas import read_csv
import numpy

data = read_csv('movie_metadata.csv', header=None)

print(data.head())