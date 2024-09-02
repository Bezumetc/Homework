#Словари и множества
my_dict = {'Adam':1957,'Barry':1999,'Chris':2010}
print(my_dict)
print(my_dict['Chris'])
print(my_dict.get('Theodor'))
my_dict.update({'Eva':1991,'Frodo':2968})
a = my_dict.pop('Chris')
print(a)
print(my_dict)

my_set = {'a',1,True,'a',True,'pool',5,1,(1,2,3),(1,2,3)}
print(my_set)
my_set.add(7)
my_set.add('line')
my_set.remove(1)
print(my_set)