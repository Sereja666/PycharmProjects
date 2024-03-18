"""
Учитывая целочисленный массив nums и целочисленное значение, удалите все вхождения val в nums на месте. Порядок
элементов может быть изменен. Затем верните количество элементов в виде чисел, которые не равны val.

Учитывайте количество элементов в nums, которые не равны val be k. Чтобы вас приняли, вам необходимо сделать следующее:

    Измените массив nums так, чтобы первые k элементов nums содержали элементы, не равные val. Остальные элементы nums
не важны, как и размер nums.
    Вернуть К.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for  el in nums:
            if el != val:
                nums[i] = el
                i+=1


        return i

nums =[0,1,2,2,3,0,4,2]
val = 2

solution = Solution()
result = solution.removeElement(nums, val)
assert result == 5, [0,1,4,0,3]
