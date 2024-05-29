"""
Напишите функцию для поиска самой длинной строки общего префикса среди массива строк.
Если общего префикса нет, верните пустую строку "".

 Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        unswer = ''
        for el in zip(*strs):
            if len(set(el)) == 1: # Если сет (1, 1, 1) равен (1) то плюсуем и идём к сд
                unswer += el[0]
            else:
                break
        return unswer




s = ["flower","flow","flight"]
solution = Solution()
result = solution.longestCommonPrefix(strs=s)
# assert result == "fl"