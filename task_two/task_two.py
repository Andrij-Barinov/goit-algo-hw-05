def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0  # Лічильник ітерацій
    upper_bound = None  # Верхня межа

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid]  # Оновлюємо верхню межу
        else:
            return (iterations, arr[mid])  # Знайшли елемент, повертаємо кількість ітерацій та елемент

    # Якщо елемент не знайдений, повертаємо кількість ітерацій і найближчу верхню межу
    return (iterations, upper_bound)

# Приклад використання
arr = [1.5, 3.2, 4.8, 6.1, 7.4, 9.0, 11.5, 13.7, 15.2, 18.4, 20.1]
x = 10.0
result = binary_search(arr, x)

print(f"Iterations: {result[0]}, Upper bound: {result[1]}")
