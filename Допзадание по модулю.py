grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)   #выполнено по условию задачи. Как я понимаю, команда sorted автоматически превращает множество в список.
students = sorted(students) #посмотрел в сети. Не додумался, как отсортировать список не вручную и без специальнх функций. Если есть вариант для новичков - подскажите.
average_score=[(sum(grades[0])/len(grades[0])),     # Смутил этот кусок кода.
               (sum(grades[1])/len(grades[1])),     # Думал, что можно через срезы сократить, но не вышло.
               (sum(grades[2])/len(grades[2])),     # Если есть другой вариант нашего уровня - подскажите, пожалуйста.
               (sum(grades[3])/len(grades[3])),     # Есть варианты через функции def/for и lambda,
               (sum(grades[4])/len(grades[4]))]     # Но до циклов еще далеко, очень их жду.

dict_average_score={}                                     # Так же по условиям задания.
dict_average_score.update({students[0]:average_score[0],  # Можно, конечно, через dict(zip(...)),
                           students[1]:average_score[1],  # но,опять же, этого не было в материале.
                           students[2]:average_score[2],  # Старался использовать только освоенные методы,
                           students[3]:average_score[3],  # чтобы показать усвоение материала.
                           students[4]:average_score[4]})
print(dict_average_score)