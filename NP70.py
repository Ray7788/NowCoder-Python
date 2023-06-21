cities_dict = {
    'Beijing': {'Capital': 'China'},
    'Moscow': {'Capital': 'Russia'}, 
    'Paris': {'Capital': 'France'}
    }

for i in sorted(cities_dict.keys()):
    print(f"{i} is the capital of {cities_dict[i]['Capital']}!")  # 字典
