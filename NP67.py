operators_dict = {'<': 'less than', '==': 'equal'}
print('Here is the original dict:')

for key, value in sorted(operators_dict.items()):
    print(f'Operator {key} means {value}.')

operators_dict['>'] = 'greater than'
print()
print('The dict was changed to:')

for key, value in sorted(operators_dict.items()):
    print(f'Operator {key} means {value}.')
