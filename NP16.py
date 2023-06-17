offer_list = ["Allen","Tom"]
for i in offer_list:
    print(i + ', you have passed our interview and will soon become a member of our company.' )
    
offer_list.remove('Tom')
offer_list.append('Andy')
for j in offer_list:
    print(j + ', welcome to join us!')
