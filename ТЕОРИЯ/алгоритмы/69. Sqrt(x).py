"""Учитывая неотрицательное целое число x, верните квадратный корень из x, округленный до ближайшего целого числа.
Возвращаемое целое число также должно быть неотрицательным.
Вы не должны использовать какие-либо встроенные функции или операторы экспоненты.
    Например, не используйте pow(x, 0.5) в C++ или x** 0.5 в Python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:

    0 <= x <= 231 - 1

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while right>=left:
            middle = (right+left)//2
            if middle*middle>x:
                right= middle- 1
            else:
                left = middle+1
        return left-1


x = 8

solution = Solution()
result = solution.mySqrt(x)
assert result == 2
