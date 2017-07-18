

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        re_x = str(x)[::-1]
        if re_x == str(x):
            return True
        else:
            return False