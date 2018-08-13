

# Calculating the central tendency
# Method 1 - Arithmetic Mean

# Extract all of the scores from dataset
scores = [float(w[4]) for w in wines[1:]]
# Sum up all the scores
sum_scores = sum(scores)
# Get the number of observations
num_scores = len(scores)
# Calculating the mean
avg_score = sum_scores/num_scores
print("Arithmetic Mean of the scores for wines is ", avg_score) # This is the Arithmetic Mean (Central Tendency Method 1)

# Calculating the central tendency
# Method 2 - Median

# Taking prices of wines from dataset
prices = [float(w[5]) for w in wines[1:] if w[5]!='']
# FInd the number of prices
num_wines = len(prices)
# Sort the wine price in ascending order
sorted_price = sorted(prices)
# Calculate the middle index
middle = int((num_wines/2)+0.5)
# Print the median of the prices
print("Median of Prices of Wines is ", sorted_price[middle])
print("Arithmetic mean of Wines is ", sum(prices)/num_wines)

# Here we can see that the median and mean are far different.
# This is due to outliers. Lets find the outliers in the Dataset

min_wine_price = min(prices)
max_wine_price = max(prices)
print("Minimum Wine cost is ", min_wine_price)
print("Maximum Wine cost is ", max_wine_price)

# Calculating the central tendency
# Method 3 - Mode

# The mode is defined as the value that appears the most frequently in our data.
price_count = [0]*int(max(prices)+1)
for p in prices:
    price_count[int(p)] += 1
print(price_count)
print("Maximum occurrence of a price is", max(price_count), "times")
print("And that price is ", price_count.index(max(price_count)))

# We notice that mode is close to median than mean. So we take median and mode for confidence
