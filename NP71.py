result_dict = {
    'Allen': ['red', 'blue', 'yellow'], 
    'Tom': ['green', 'white', 'blue'], 
    'Andy': ['black', 'pink']
    }

for i in sorted(result_dict.keys()):
    colors = result_dict[i]
    print(f"{i}'s favorite colors are:")
    for color in colors:
        print(color)
