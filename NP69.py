my_dict_1 = {'name': 'Niuniu', 'Student ID': 1}
my_dict_2 = {'name': 'Niumei', 'Student ID': 2}
my_dict_3 = {'name': 'Niu Ke Le', 'Student ID': 3}
dict_list = []
dict_list.append(my_dict_1)
dict_list.append(my_dict_2)
dict_list.append(my_dict_3)

for i in dict_list:
    # 字典获取元素的方法i['key值']，或者i.get('key值')
    print(f"{i['name']}'s student id is {i.get('Student ID')}.")
