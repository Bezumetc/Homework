#Изменяемые и неизменяемые элементы. Кортежи.
immutable_war = (1,2,3,True,'Urban') #кортеж
print(immutable_war)
#immutable_war[0] = 10 # - ошибка, нельзя изменить неизменяемый элемент кортежа
#print (immutable_war)
immutable_war = ([1,2],3,True,'Urban')
immutable_war[0][1] = 10 #корректно, т.к. в неизменяемом кортеже есть изменяемый элемент "список"
print(immutable_war)
mutable_list = [1,2,3,True,'Urban'] #список
mutable_list[0] = 10
mutable_list[3] = False
mutable_list[-1] = 0.5
print(mutable_list)
