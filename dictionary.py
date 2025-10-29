
my_dict = {}


my_dict = {1: 'pinaapple', 2: 'ball'}

print(my_dict)
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)
my_dict = {'name': 'Jack', 'age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 35
print(my_dict)
my_dict['address'] = 'Park Street'
print(my_dict)
my_dict.pop('age')
print(my_dict)
print("Address :", my_dict.get('address'))
my_dict.clear()
print(my_dict)




