"""
Учитывая заголовок отсортированного связанного списка, удалите все дубликаты, чтобы каждый элемент появлялся только
один раз. Верните связанный список также отсортированным.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cursor = head
        while cursor and cursor.next:
            if cursor.val == cursor.next.val: # если курсор равен следующему курсору, то  / \
                cursor.next = cursor.next.next # следующий назначаем курсор через один   1 2 3 4
            else:
                cursor = cursor.next
        return head


def printLinkedList( head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Проверка работы метода deleteDuplicates
list1 = ListNode(1)
list1.next = ListNode(1)
list1.next.next = ListNode(2)

solution = Solution()
result = solution.deleteDuplicates(list1)

printLinkedList(result)