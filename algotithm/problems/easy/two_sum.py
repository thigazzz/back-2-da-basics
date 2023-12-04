"""
Dada uma matriz de números inteiros e um destino inteiro, retorne índices dos dois números de forma que eles se somem ao destino.

Você pode supor que cada entrada teria exatamente uma solução e não pode usar o mesmo elemento duas vezes.

Você pode retornar a resposta em qualquer ordem.
"""

from typing import List

class Solution:
    def my_two_sum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        while index < len(nums):
            for num_i, num in enumerate(nums):
                if index == num_i:
                    continue
                if nums[index] + num == target:
                    return [nums.index(nums[index]), num_i]
            index += 1

    def other_two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # Percorre Um numero
            for j in range(i + 1, len(nums)): # Percorre todos os numero
                if (nums[i] + nums[j] == target):
                    return [i,j]

    



assert Solution().my_two_sum([2,7,11,15], 9) == [0,1]
assert Solution().my_two_sum([3,2,4], 6) == [1,2]
assert Solution().my_two_sum([3,3], 6) == [0,1]
assert Solution().my_two_sum([3,2,3], 6) == [0,2]

assert Solution().other_two_sum([2,7,11,15], 9) == [0,1]
assert Solution().other_two_sum([3,2,4], 6) == [1,2]
assert Solution().other_two_sum([3,3], 6) == [0,1]
assert Solution().other_two_sum([3,2,3], 6) == [0,2]

print("COMPLETO")
# COMPLETO