
#num1 = 3 * True - (True + False)
#num2 = (True + True + False) ** 3 + 5
#print(num1 + num2)
    """_summary_
numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
res = 0
for num in numbers:
    res += (num % 2 == 1) and (num > 1)
print(res)

#пример буллион (7;6)
def is_even(num):
    return num % 2 == 0

#инстинанс проверяет тип данных
print(isinstance(3, int))
print(isinstance(3.5, float))
print(isinstance('Beegeek', str))
print(isinstance([1, 2, 3], list))
print(isinstance(True, bool))

#Функция type() выводит тип данных
print(type(3))
print(type(3.5))
print(type('Beegeek'))
print(type([1, 2, 3]))
print(type(True))
    Returns:
        _type_: _description_
    """

list1 = [[1, 2, 3], [4, 5], [8], [1, 2, 3, 4]]
print(len(list1))
