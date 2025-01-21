team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print('В команде %s участников %d' % (team1_name, team1_num))
print('В команде %s участников %d' % (team2_name, team2_num))
print('Итого сегодня в командах участников %d и %d' % (team1_num, team2_num))
print('Команда {} решила задач {}'.format(team1_name, score_1))
print('Команда {} решила задач {}'.format(team2_name, score_2))
print('{} решили задачи за {}'.format(team1_name, team1_time))
print('{} решили задачи за {}'.format(team2_name, team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')