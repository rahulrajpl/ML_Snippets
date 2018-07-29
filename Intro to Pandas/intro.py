import pandas
print("Hello")
print(pandas.__version__)
names = pandas.Series(['rahul', 'raj', 'parvathy'])
rolls = pandas.Series([1,2,3])

df = pandas.DataFrame({"name":names, "roll no":rolls})
print(df)

df = pandas.read_csv("california_housing_train.csv", sep=',')
print(df.describe())