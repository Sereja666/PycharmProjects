"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
 is not part of haystack.
Учитывая две строки иглы и стога сена, верните индекс первого вхождения иглы в стоге сена или -1, если игла
 не является частью стога сена.


Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.



Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.


"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle in haystack:
        #     for index, val in enumerate(haystack):
        #
        #         if needle not in haystack[index:]:
        #             return index-1
        stop = 0
        if needle in haystack:
            if haystack == needle:
                return 0
            for i, val in enumerate(haystack):

                if val == needle[0]:
                    for index, item in enumerate(needle):
                        if item == haystack[i + index]:
                            stop += 1
                            if stop == len(needle):
                                return i
                        else:
                            stop = 0
                            break

        else:
            return -1




haystack = "sadbutsad"
needle = "sad"
solution = Solution()
result = solution.strStr(haystack, needle)
assert result == 0
