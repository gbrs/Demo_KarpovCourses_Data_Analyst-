'''
Строка names содержит имена в формате 'Name1 Surname1, Name2 Surname2, …'.
Поместите в переменную names_list список со строками имён –
['Name1 Surname1', 'Name2 Surname2', …]
'''

names = 'Name1 Surname1, Name2 Surname2'
names_list = names.split(', ')

print(names_list)
