# Задача 1. Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001


print('Число Пи с заданной точностью d') 
def GetNumber():
    try:
        x = abs(int(input('Введите целое число n от 1 до 10, для определения точности вычисления Пи : ')))
        return x 
    except:
        print('Целое число введено неверно, введите число еще раз')    
        return GetNumber()

n = GetNumber()
while not (1<=n<=10):
    n = GetNumber()
d = 10 ** (-n)
Pi = 0
x = 1
singn = 1
while True:
    a = 4/x 
    Pi = Pi+singn*a
    if a<d:
        break
    singn=-singn
    x=x+2
print (round(Pi, n))

print()
print()


# Задача 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.


print('Список простых множителей') 
import math

def CheckNumber(number):
    flag = True
    for i in range(2, math.ceil(math.sqrt(number))):
        flag = bool(number % 1)
        if not flag:
            break
    return flag

def FindDiviger(number):
    divigers = []
    for i in range(2, number//2):
        while CheckNumber(i) and number % i == 0:
            if number % 1 == 0 and CheckNumber(i):
                divigers.append(i)
                number /= i

    print(divigers)

number =243 
FindDiviger(number)         

print()
print()



# Задача 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]


print('Список неповторяющихся элементов исходной последовательности') 
print('Введите числа через пробел')
list1 = list (map(int, input().split()))
list2 = []
for i in list1:
    if list1.count (i) ==1:
        list2.append(i)
print(list2)
    
print()
print()    

# # Задача 4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов  (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


print('Список коэффициентов, сформированных случайным образом, и запись многочлена степени k') 
import random
dict = {
    0: "\u2070",
    1: "\u0089",
    2: "\u0082",
    3: "\u0083",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079",
}

k = int (input("Задайте натуральную степень k от 1 до 9: "))

ind = []
for i in range(k+1):
    ind.append(random.randint(0, 100))
print(f'Список коэффициентов: {ind}')
s = ''

for i in range(len(ind) - 1):
    if ind [i] !=0:
        if (k-1) == 1:

            s += str(ind[i]) + "x + "
        else:
            s += str(ind[i]) + "x^" + str(k - i)+' + '

itog = s + str(ind[-1])+" = 0" 
print(itog)
print("Результат сохранен в файде file1.txt")

file = open("file1.txt", "a")
file.write(itog)
file.write('\n')
file.close()

print()
print()  


# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0



print('Сумма двух многочленов') 
def get_lst(file: str) -> list:
    with open(file, 'r') as f:
        s = f.readline()[:-4]
        print(s)
    s = s.replace('+ ', '+').replace('- ', '-')
    if s[0] != '-':
        s = '+' + s
    return s.split()

def get_dict(lst: list) -> dict:
    dct = {}
    for i in lst:
        sign = i[0]
        i = i[1:]
        coef = i 
        power = 0
        if 'x' in i:
            coef = i.split('x')[0] if i.split('x')[0] else [1]
            if '^' in i:
                power = int(i.split('^')[1])
            else:
                power = 1
        dct[power] = [sign, coef]
    return dct 

def sum_els(lst_a: list, lst_b: list) -> list or None:
    sign_a, sign_b = lst_a[0], lst_b[0]
    coef_a, coef_b = int(lst_a[1]), int(lst_b[1])
    if sign_a == '+' and sign_b == '+':
        coef = coef_a + coef_b
    elif  sign_a == '+' and sign_b == '-':   
        coef = coef_a - coef_b
    elif sign_a == '-' and sign_b == '+': 
        coef = - coef_a + coef_b
    else:
        coef = - coef_a - coef_b

    if coef > 0:
        return ['+', str(coef)]
    elif coef < 0:
        return['-', str(coef)[1:]]
    else:
        return None

a, b = map(get_lst, ['file2.txt', 'file3.txt'])
print(a, b, sep = '\n')
a, b = map(get_dict,[a, b])
print(a, b, sep='\n0')

for k,v in b.items():
    if k not in a:
        a[k] = v 
    elif sum_els(a[k], v):
        upd_elt = sum_els(a[k], v)
        a[k] = upd_elt
    else:
        del a[k]

res = ''
for k, v in sorted(a.items(), reverse=True):
    if k > 1 and v[1] != '1':
        res += f' {v[0]} {v[1]}x^{k}'
    elif k > 1:
        res += f' {v[0]} x^{k}'
    elif k == 0:
        res += f' {v[0]} {v[1]}'
    elif k == 1 and v[1] != '1':
        res += f' {v[0]} {v[1]}x'
    elif k == 1:
        res += f' {v[0]} x'

if not res:
    res = '0 = 0'
elif res[0:2] == ' +':
    res = res[3:] + ' = 0'

print(res)

with open('file4.txt', 'a') as f:
    f.write(res)










