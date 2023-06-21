entry_form = ('Niuniu', 'Niumei')
print(entry_form)

try:
    entry_form[1] = 'Niukele'
except TypeError:
    print('The entry form cannot be modified!')
