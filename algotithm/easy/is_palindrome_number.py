"""
Retornar True se o número for Palindromo

Os números palíndromos são números que podem ser lidos em ordem inversa e continuam tendo o mesmo valor.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        normal_order = str(x)
        reversed_order = normal_order[::-1]
        if normal_order == reversed_order:
            return True
        
        return False
        

assert Solution().isPalindrome(121) == True
assert Solution().isPalindrome(-121) == False
assert Solution().isPalindrome(10) == False