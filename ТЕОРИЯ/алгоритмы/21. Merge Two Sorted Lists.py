"""
Вам даны заголовки двух отсортированных связанных списков list1 и list2.
Объедините два списка в один отсортированный список. Список должен быть составлен путем сращивания узлов первых двух списков.
Возвращает заголовок объединенного связанного списка.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val= 0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
     -> 1  2,  4
        | /| / |
        1  3   4
    привязываемся не к значению, а к курсору. Начинаем с первого элемента одно из списоков, сравниваем его со элементом
    из второго списка меньший элемент записываем в список dummy, курсор переносим на элемент который был больше
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next # сдвигаем элемент

        tail.next = list1 or list2 # если списоки разные по длине, то остаток перемещается в "хвост"

        return dummy.next

# Создаем узлы для списков list1 и list2
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(6)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Вызываем метод mergeTwoLists и проверяем результат
solution = Solution()
result = solution.mergeTwoLists(list1, list2)

# Проверяем результат
output = []
while result:
    output.append(result.val)
    result = result.next

assert output == [1, 1, 2, 3, 4, 4, 6]