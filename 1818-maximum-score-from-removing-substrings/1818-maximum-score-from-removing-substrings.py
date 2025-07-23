class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def helper(pair, score):
            nonlocal s
            stack=[]
            dy=0
            for el in s:
                if el == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    dy+=score
                else:
                    stack.append(el)
            s = "".join(stack)
            return dy

        dx=0
        pair = "ab" if x>y else "ba"
        dx+=helper(pair, max(x, y))
        dx+=helper(pair[::-1], min(x, y))
        return dx

        