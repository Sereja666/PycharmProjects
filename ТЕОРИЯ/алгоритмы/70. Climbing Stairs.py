"""Вы поднимаетесь по лестнице. Чтобы достичь вершины, нужно n шагов.

Каждый раз вы можете подняться на 1 или 2 ступеньки. Сколькими различными способами вы можете подняться на вершину?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step



Constraints:

    1 <= n <= 45

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return 2
        step1 = 1
        step2 = 2
        for _ in range(2, n):
            corrent = step1 + step2
            step1 = step2
            step2 = corrent
        print(corrent) #2971215073
        return corrent

class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5=(5)**(1/2)
        fibn=((1+sqrt5)/2)**(n+1)-((1-sqrt5)/2)**(n+1)
        print(int(fibn/sqrt5))
        return int(fibn/sqrt5)

n = 4
solution = Solution()
result = solution.climbStairs(n)
# assert result == 4
