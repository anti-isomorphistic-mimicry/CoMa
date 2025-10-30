# Robert Jerye studonid: uz67izax

#user input
print('Gib eine positive ganze Zahl ein: ', end='')
variable = int(input())

#setup divider list and append actual dividers
div_list=[]

for i in range(1,variable):
    if int(variable)%i==0: div_list.append(i)

#sum up dividers and compare to input, output dividers and perfect number case
total = sum(div_list)
print('Die Teiler von ', variable, ' sind: ', end='')
for i in range(1,len(div_list)-1):
    print(i,end=', ')
print(div_list[len(div_list)-1])
print('Die Summe der Teiler ist: ', total)

if total==variable: print(variable, ' ist eine perfekte Zahl!')
else: print(variable, ' ist keine perfekte Zahl!')
