"""
Дана строка s, состоящая из слов и пробелов, верните длину последнего слова в строке.

Слово – это максимум подстрока
состоящий только из символов, не являющихся пробелами.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.



Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.


"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        index = len(s) - 1
        while s[index] == " ":
            index-=1
        while index >=0 and s[index] != ' ':
            count+=1
            index-=1
        return count



s = "   fly me   to   the moon  "
solution = Solution()
result = solution.lengthOfLastWord(s)
assert result == 4
