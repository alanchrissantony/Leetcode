class Solution:
    def isPalindrome(self, s: str) -> bool:
        dp=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        st=""
        for el in s:
            if el in string.ascii_lowercase or el in string.ascii_uppercase or el in dp:
                try:
                    st+=el.lower()
                except:
                    st+=el
    
        return st==st[::-1]
