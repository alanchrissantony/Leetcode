class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dx={el:i for i, el in enumerate(string.ascii_uppercase, 1)}
        rst=0
        for el in columnTitle:
            rst=rst*26+dx[el]
        return rst