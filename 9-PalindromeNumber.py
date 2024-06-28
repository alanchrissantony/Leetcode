class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        def check(string):
            return string == string[::-1]
        return(check(string))
