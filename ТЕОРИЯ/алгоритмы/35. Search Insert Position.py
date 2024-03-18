"""
Учитывая отсортированный массив различных целых чисел и целевое значение, верните индекс, если цель найдена. Если нет,
верните индекс там, где он был бы, если бы он был вставлен по порядку.
Вы должны написать алгоритм со сложностью выполнения O(log n).


Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums)-1
        while left_index<=right_index:
            mid = (left_index+right_index)//2
            if target > nums[mid]:
                left_index=mid+1
            else:
                right_index = mid-1
            print(left_index, mid, right_index)
        return left_index


nums = [3,6,7,8,10]
target = 8
solution = Solution()
result = solution.searchInsert(nums, target)
assert result == 3

