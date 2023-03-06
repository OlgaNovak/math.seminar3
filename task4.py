# В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же,
# сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию. 
# Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

pa=0.8
pb=0.7
pc=0.9

# По формуле Байеса:

P1=1/4*pa/(1/4*pa+1/4*pb+1/2*pc)
P2=1/4*pb/(1/4*pa+1/4*pb+1/2*pc)
P3=1/2*pc/(1/4*pa+1/4*pb+1/2*pc)
print(f'Вероятность, что студент c факультета A: {P1}')
print(f'Вероятность, что студент c факультета B: {P2}')
print(f'Вероятность, что студент c факультета C: {P3}')