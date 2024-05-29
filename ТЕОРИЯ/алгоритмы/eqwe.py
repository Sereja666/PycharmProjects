"""
Дан список целых чисел, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку,
сворачивая соседние по числовому ряду числа в диапазоны.

Примеры:
- [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"
- [1, 4, 3, 2] => "1-4"
- [1, 4] => "1,4"
- [1]
"""


def compress(l):
    my_string = ''
    my_list = []
    l.sort()

    numb_list = 1
    for index, val in enumerate(l[:-1]):

        if val + 1 == l[index + 1]:
            my_list[numb_list].append(val)

        else:
            my_list[numb_list].append(val)
            numb_list += 1
        # [[1]]
        # [[0, 1, 2,3,4,5],[8,9],[11]
    for l1 in my_list:
        if len(l1) > 1:
            my_string += l1[0] + '-' + l[:-1]

        else:
            my_string += l1[0]
    return my_string.rstrip(",")
# def compress(l):
#     start_val = min(l)
#     end_val = max(l)
#     print(start_val)
#     big_list = []
#     n_list = 0
#     for i in range(start_val, end_val):
#         temp_list = []
#         if i in l:
#             temp_list[n_list] = temp_list.append()
#         else:
#             n_list+=1
#     print(temp_list)

compress([1, 4, 5, 2, 3, 9, 8, 11, 0])