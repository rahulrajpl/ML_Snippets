import csv
with open("winemag-data_first150k.csv", 'r', encoding='latin-1') as f:
    wines = list(csv.reader(f))

# Measure of dispersion
# Taking prices of wines from dataset for studying range and Interquartile range
prices = [float(w[5]) for w in wines[1:] if w[5]!='']

# Range of the price
# -------------------
print("Range of the price is max-min:", max(prices)-min(prices))
# This means data is extremely spread out
# But this is independent of central tendency. So it's least helpful

# Standard Deviation
# ------------------
mean_price = sum(prices)/len(prices)
d = 0
for p in prices:
    d += (p-mean_price) ** 2
sd = (d/(len(prices)))**0.5
print("Standard Deviation of price is ", sd)

# Variance
# --------
print("Variance of the price is ", sd*sd)