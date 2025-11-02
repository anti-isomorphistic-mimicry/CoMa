#data list
data = [ [3, 5, 2,5], [10, 15, 10], [8, 8, 8, 8], [7, 2, 9, 2, 7] ]

# A1.1 

print('\nAufgabe 1.1')

element_count = []
for i in range(len(data)):
    element_count.append(len(set(data[i])))

print('Anzahl verschiedener Zahlen:', element_count, end='\n\n')

# A1.2

print('Aufgabe 1.2')

max_list = []

for i in range(len(data)):
    max_list.append(max(data[i]))

print('Größte Zahlen:', max_list, end='\n\n')

# A1.3
concat_list = []
print('Aufgabe 1.3')

for i in range(len(data)):
    concat_list = concat_list+data[i]

concat_list =sorted(concat_list)
print('Alle Zahlen sortiert:', concat_list, end='\n\n')

# A1.4

print('Aufgabe 1.4')

set_data =set(concat_list)

#Creating a dictionary with set elements as keys and a start counter of 0
nunique_dict ={}
for i in set_data:
    nunique_dict[i]=0

#sorting and counting all elements
for i in range(len(data)):
    for j in range(len(data[i])):
        nunique_dict[data[i][j]] = nunique_dict[data[i][j]] +1

#identifying the keys with the max count
max_keys = [key for key, val in nunique_dict.items() if val == max(nunique_dict.values())]
print('Häufigste:', min(max_keys), end='\n\n')