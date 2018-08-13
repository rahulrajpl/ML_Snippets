from math import log
# Program to find the entropy and Information Gain of the DataSet

days = list(range(1,15))
# sunny = 1 # overcast = 2 # rain = 3
outlook = [1,1,2,3,3,3,2,1,1,3,1,2,2,3] # Feature 1
# hot = 1 # mild = 2 # cool = 3
temperature = [1,1,1,2,3,3,3,2,3,2,2,2,1,2]# Feature 1
# high = 1 # normal = 2
humidity = [1,1,1,1,2,2,2,1,2,2,2,1,2,1]# Feature 1
# weak = 1 # strong = 2
wind = [1,2,1,1,1,2,2,1,1,1,2,2,1,2] # Feature 1
# LABEL PLAY=1 NOPLAY=0
play = [0,0,1,1,1,0,1,0,1,1,1,1,1,0]

# Calculate the entropy and Information gain of each feature
def calculate_rootentropy(feature):
    h = 0
    for i in set(feature):
        h += (feature.count(i)/ len(feature)) * log(feature.count(i)/ len(feature), 2)
    return -h

def calculate_entropy_and_IG(root_h, feature):
    h_f = []
    for f in set(feature):
        p = [i for i,j in zip(play, feature) if j is f]
        try:
            h = [(p.count(i) / len(p)) * log(p.count(i) / len(p), 2) for i in set(play) if (p.count(i) / len(p)) > 0]
        except:
            pass
        # print("Entropy of", "Weak" if f is 1 else "Strong", -sum(h))
        h_f.append(-sum(h))
    ig = root_h
    for i in h_f:
        a = feature.count(h_f.index(i)+1)
        b = len(feature)
        ig -= (a/b) * i
    return ig

def main():
    # Calculate root entropy ie. Entropy of Play
    root_h = calculate_rootentropy(play)
    print("Entropy of Root is", root_h)
    features = [outlook, temperature, humidity, wind]
    feature_cols = ["Outlook", "Temperature", "Humidity", "Wind"]
    for feature in features:
        print("IG (", feature_cols[features.index(feature)],") = ", calculate_entropy_and_IG(root_h, feature))


if __name__ == "__main__":
    main()