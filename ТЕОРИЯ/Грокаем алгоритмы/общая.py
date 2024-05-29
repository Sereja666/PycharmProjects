import math

x = 1_000_000_000
result = int(math.log(x, 2))
print("Логарифм числа", x, "по основанию", 2, "равен", result)


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    i = 0
    while low <= high:
        i +=1
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid, i
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = range(1_000_000_000)

print(binary_search(my_list, 879556))
print(binary_search(my_list, -1))