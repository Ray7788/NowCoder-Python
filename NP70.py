cities_dict = {
    'Beijing': {'Capital': 'China'},
    'Moscow': {'Capital': 'Russia'}, 
    'Paris': {'Capital': 'France'}
    }

for i in sorted(cities_dict.keys()):
    print(f"{i} is the capital of {cities_dict[i]['Capital']}!")  # 字典：先访问cities_dict 再访问其中一个的capital 再访问对应的国家
