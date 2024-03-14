"""Учитывая массив целых чисел nums и целочисленную цель, верните индексы двух чисел так, чтобы их сумма составляла цель.

Вы можете предположить, что каждый вход будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.

Вы можете вернуть ответ в любом порядке."""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, el in enumerate(nums):
            for i_nums in range(index + 1, len(nums)):
                if el + nums[i_nums] == target:
                    print(f'{index}: {el} + {i_nums}: {nums[i_nums]} = {target} ')
                    return [index, i_nums]


my_list = [2, 5, 7, 1]
solution = Solution()
result = solution.twoSum(nums=my_list, target=9)

assert list(result) == [0, 2]

# ------------------------ Вариант 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]