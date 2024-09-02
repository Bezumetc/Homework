first=int(input('Введите 1ое число: '))
second=int(input('Введите 2ое число: '))
third=int(input('Введите 3е число: '))
if first==second and first==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)