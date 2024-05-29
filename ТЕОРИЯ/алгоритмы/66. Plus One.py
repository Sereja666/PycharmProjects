"""Вам дано большое целое число, представленное в виде целочисленного массива цифр, где каждая digit[i] — это i-я цифра
целого числа. Цифры упорядочены от наиболее значимого к наименее значимому, слева направо. Большое целое число не
содержит ведущих нулей.

Увеличьте большое целое число на единицу и верните полученный массив цифр.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].



Constraints:

    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain any leading 0's.

"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        for item in digits[::i]:
            if item+1 >=10:
                digits[i] = (item+1)%10

                if -(i-1) <= len(digits):
                    digits[i-1] = item+1
                else: digits.insert(0, 1)
                i-=1
                print(digits)
            else:
                digits[i] = item+1
                break
        print(digits)
        return digits


digits = [9,9]
solution = Solution()
result = solution.plusOne(digits)
# assert result == [1,0,0]
