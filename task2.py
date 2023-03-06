# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

from math import factorial
def combination (n,k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

Pa1=combination(5,2)*combination(3,0)/combination(8,2)     # 1 случай, из корзины А взяли 2 белых шара
Pb1=combination(5,1)*combination(7,3)/combination(12,4)    # 1 случай, из корзины В взяли 1 белый шар
Pa2=combination(5,1)*combination(3,1)/combination(8,2)     # 2 случай, из корзины А взяли 1 белый шар
Pb2=combination(5,2)*combination(7,2)/combination(12,4)    # 2 случай, из корзины В взяли 2 белых шара
Pa3=combination(5,0)*combination(3,2)/combination(8,2)     # 3 случай, из корзины А взяли 0 белых шаров
Pb3=combination(5,3)*combination(7,1)/combination(12,4)    # 3 случай, из корзины В взяли 3 белых шара
P=Pa1*Pb1+Pa2*Pb2+Pa3*Pb3
print(f'Вероятность, что 3 мяча белые:{P}')