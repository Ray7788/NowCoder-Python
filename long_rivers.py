rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

# 1. In a for loop, print out each river's name!
for i in rivers:
    print(i["name"])
total_length = 0

# 2. In another for loop, add up and print out the total length of all the rivers!
for i in rivers:
    total_length += i["length"]
print(total_length)

# 1. Print out every river's name that begins with the letter M !
for i in rivers:
    if i["name"][0] == "M":
        print(i["name"])

# 2. The length of the rivers are in miles. Print out every river's length in kilometres! (1 mile is
# roughly 1.6 km)
for i in rivers:
    print(i["length"]*1.6)
