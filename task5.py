# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
# Какова вероятность того, что в первый месяц выйдут из строя: а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

p1=0.1
p2=0.2
p3=0.25
q1=1-p1
q2=1-p2
q3=1-p3

P1=p1*p2*p3
P2=p1*p2*q3+p1*q2*p3+q1*p2*p3
P3=1-q1*q2*q3
P4=P2+(p1*q2*q3+q1*p2*q3+q1*q2*p3)
print(f'Вероятность, что в 1 месяц все детали выйдут из строя: {P1}')
print(f'Вероятность, что в 1 месяц только 2 детали выйдут из строя: {P2}')
print(f'Вероятность, что в 1 месяц хотя бы 1 деталь выйдет из строя: {P3}')
print(f'Вероятность, что в 1 месяц от 1 до 2 деталей выйдут из строя: {P4}')
