#2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
#  Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.

n=int(input("Insert  quantity of coins"))

count = 0
for i in range(n):
    coin = int(input('Insert result  - "0" or - "1": '))
    count += coin
    i += 1
if count <= n//2:
    print('Minimum quantity of coins need to be replaced is  ', count)
else:
    print('Minimum quantity of coins need to be replaced is ', n - count)



