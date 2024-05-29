
# Алгаритмы - последовательность действий
#
# Онатация - говорит нам как будет изменяться работа алгоритма при увеличении входных данных


"""
O(1) - констрантная сложность
O(n) - линейная, сколько элементов переданно такая и сложность
O(n*3) - квадратичная, сколько for
O(e*n) - экспоненциальная сложность (супер рост)
O(log(n)) - логарифмическа сложность (бинарный поиск и обход деревьев)

"""
#                               Быстрая сортировка
def quicksort(arr):
    """Быстрая сортировка: Быстрая сортировка — это алгоритм «разделяй и властвуй»,
     который выбирает «основной» элемент из массива и разбивает остальные элементы
      на два подмассива. Затем подмассивы сортируются рекурсивно."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  #  ну или рандомный id взять
    left = [x for x in arr if x < pivot]
    print(left)
    middle = [x for x in arr if x == pivot]
    print(middle)
    right = [x for x in arr if x > pivot]
    print(right)
    return quicksort(left) + middle + quicksort(right)

# print(quicksort([3, 6, 8, 10, 1, 2, 1]))
# =======================================================================================================================

#                               Сортировка слиянием
# Сортировка слиянием: Алгоритм сортировки слиянием — это алгоритм «разделяй и властвуй»,
# который делит массив на две части, сортирует две половины, а затем снова объединяет их.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
# print(merge_sort([3,6,8,10,1,2,1]))
# =======================================================================================================================
#                                           Бинарный поиск
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
# print(binary_search([1,2,3,4,5,6,7], 6))
# =======================================================================================================================
#                           Последовательность Фибоначчи
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(10))
# =======================================================================================================================
