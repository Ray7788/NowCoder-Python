current_users =['Niuniu','Niumei','GURR','LOLO']
new_users =['GurR','Niu Ke Le','LoLo','Tuo Rui Chi']

for i in new_users:
    for j in current_users:
        if i.upper()==j.upper():    # 不区分大小写
            print('The user name %s has already been registered! Please change it and try again!'% i)
            break
    else:
        print('Congratulations, the user name %s is available!'% i)
