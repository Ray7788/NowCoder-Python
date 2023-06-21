survey_list = ['Niumei', 'Niu Ke Le', 'GURR', 'LOLO']
result_dict = {'Niumei': 'Nowcoder', 'GURR': 'HUAWEI'}

for i in survey_list:
    if i in result_dict.keys():
        print(f'Hi, {i}! Thank you for participating in our graduation survey!')
    else:
        print(f'Hi, {i}! Could you take part in our graduation survey?')
