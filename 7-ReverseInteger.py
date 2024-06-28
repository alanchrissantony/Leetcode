class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = x[::-1]
        stdout = ""

        for i in x:
            if "-" == i:
                stdout = "-" + stdout
            else:
                stdout += i
        stdout = int(stdout)
        if abs(stdout) > 2147483648:
            return 0
        return stdout