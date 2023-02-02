#Задача 1: Найдите сумму цифр трехзначного числа.
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

n = input('Введите трехзначное число: ')
a = int(n[0])
b = int(n[1])
c = int(n[2])
print('Сумма цифр трехзначного числа: ', a + b + c)

# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов.
#  Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

a = int(input('Введите число: '))
k = int((a/3)*2)
p = int((k/2)/2)
s = int(p)
print(p,k,s)

# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#  Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

n = (input('Введите билет: '))
s1 = n[0] + n[1] + n[2]
s2 = n[3] + n[4] + n[5]
if s1 == s2:
  print("YES")
else:
  print("NO")

# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('введите число'))
m = int(input('введите число'))
k = int(input('введите число'))
if (k < n*m) and ((k%n == 0) or (k%m == 0)):
    print('Yes')
else:
    print('No')    