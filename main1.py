name = 'Basil' #0
surname = 'Popov' #1
age = 27 #2
temp = 36.6 #3
was_ill = False #4

data_list = [name, surname, age, temp, was_ill]
data_list_values = ['Basil', 'Popov', 27, 36.6, False]

print (data_list + data_list_values)
print (data_list)
data_list += data_list_values
print(data_list)