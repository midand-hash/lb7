# list_reordering.py

# Ввод списка вещественных чисел
n = int(input("Enter the number of elements in the list: "))
lst = [float(input(f"Enter element {i+1}: ")) for i in range(n)]

# Ввод диапазона A и B
A = float(input("Enter the lower bound (A): "))
B = float(input("Enter the upper bound (B): "))

# 1. Количество элементов в диапазоне от A до B
count_in_range = sum(A <= x <= B for x in lst)

# 2. Сумма элементов после максимального элемента
max_element = max(lst)
max_index = lst.index(max_element)
sum_after_max = sum(lst[max_index + 1:])

# 3. Упорядочивание элементов по убыванию модулей
lst_sorted = sorted(lst, key=abs, reverse=True)

# Вывод результатов
print(f"Count of elements in the range [{A}, {B}]: {count_in_range}")
print(f"Sum of elements after the maximum element ({max_element}): {sum_after_max}")
print(f"List sorted by descending absolute values: {lst_sorted}")
