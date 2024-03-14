"""
Дан ряд чисел (пример [1, 2,1,3,4,5,2,1]). Необходимо найти и вывести локальные максимумы.
 Локальным максимумом считается то числе, которое больше или равно своим соседям
"""
my_list = [1, 2, 1, 3, 4, 5, 2, 1, 7, 1, 1, 1, 7]


def foo2(list: list):
    zip_list = zip(my_list, my_list[1:len(my_list)], my_list[2:len(my_list)])
    for el_left, el_mid, el_rigt in zip_list:
        if el_mid >= el_rigt and el_mid >= el_left:
            yield el_mid


# def foo(my_list):
#     i = 0
#     for _ in range(len(my_list) - 2):
#
#         el_left = my_list[i]
#         el_mid = my_list[i + 1]
#         el_rigt = my_list[i + 2]
#         if el_mid >= el_rigt and el_mid >= el_left:
#             yield el_mid
#         i += 1


result = foo2(my_list)

assert list(result) == [2, 5, 7, 1]
# ----------------------------------------------------------------------------------------------------------------------