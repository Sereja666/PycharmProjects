"""
Учитывая числа целочисленного массива, отсортированные в неубывающем порядке, удалите дубликаты на месте так,
чтобы каждый уникальный элемент появляется только один раз. Относительный порядок элементов должен оставаться неизменным.
Затем верните количество уникальных элементы в цифрах.
Считайте, что количество уникальных элементов чисел равно k. Чтобы вас приняли, вам необходимо сделать следующее:

Измените массив nums так, чтобы первые k элементов nums содержали уникальные элементы в том порядке, в котором они были.
изначально присутствует в цифрах. Остальные элементы nums не важны, как и размер nums.
    Вернуть К.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Объяснение: Ваша функция должна возвращать k = 2, причем первые два элемента nums равны 1 и 2 соответственно.
Не имеет значения, что вы оставите после возвращенного k (следовательно, они являются подчеркиванием).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).



Constraints:

    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.


"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            k
        [0, 0, 1,1,1,2,2,3,3,4]
        берём K как указатель, проходимся по каждому элементу списка, начиная с индекса 1, сравниваем с предыдущим числом
        Получается что i убегает вперёд, если i больше предыдущего числа, то заменяем k на i, и продолжаем дальше от i
        Время O(n)
        Память O(1)
        """
        k = 1 #
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k +=1
        return k




list1 = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
result = solution.removeDuplicates(list1)
# assert result == [0,1,2,3,4,"_","_","_","_","_"]
