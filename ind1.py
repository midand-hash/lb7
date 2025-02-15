# list_sum_count.py

# Ввод списка A из 10 элементов
A = [int(input(f"Enter element {i+1} of list A: ")) for i in range(10)]

# Фильтрация элементов, удовлетворяющих условиям
filtered_elements = [x for x in A if 2 < x < 20 and x % 8 == 0]

# Подсчёт суммы и количества элементов
sum_filtered = sum(filtered_elements)
count_filtered = len(filtered_elements)

# Вывод результатов
print(f"Sum of elements greater than 2, less than 20, and divisible by 8: {sum_filtered}")
print(f"Count of such elements: {count_filtered}")
