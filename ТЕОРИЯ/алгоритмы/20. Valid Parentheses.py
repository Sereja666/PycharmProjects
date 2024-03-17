"""
Учитывая строку s, содержащую только символы '(', ')', '{', '}', '[' и ']', определите, является ли входная строка допустимой.

An input string is valid if:
    Открытые скобки должны закрываться скобками того же типа.
    Открытые скобки должны закрываться в правильном порядке.
    Каждой закрывающей скобке соответствует открытая скобка того же типа.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""
class Solution:
    # def isValid(self, s: str) -> bool:
    #     my_dict = {'(': ')', '{': '}', '[': ']',}
    #     pairs = list(zip(s[::2], s[1::2]))
    #     for el in pairs:
    #         if my_dict[el[0]] != el[1]:
    #             return False
    #     return True

    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack



s ="{[]()}"
# s = "()[]{}"
solution = Solution()
result = solution.isValid(s=s)
assert result == True