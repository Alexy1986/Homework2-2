first = input("Введите первое число ") #ввод первого числа
second = input("Введите второе число ") #ввод второго числа
third = input("Введите третье число ") #ввод третьего числа
if first == second == third:           #проверяем если все 3 числа равна
    print(3)                            #выводим 3
elif first == second or first == third: #проверяем равно ли первое число со вторым или третьим
    print(2)                            #выводим 2
elif second == first or second == third: #проверяем равно ли второе число с первым или третьим
    print(2)                            #выводим 2
elif first != second != first != third: #проверяем все 3 числа если они не равны
    print(0)                            #выводим 0
