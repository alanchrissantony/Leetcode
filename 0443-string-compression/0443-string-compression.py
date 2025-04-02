class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt, dx=1, 0
        n=len(chars)

        for i in range(1, n+1):
            if i<n and chars[i-1]==chars[i]:
                cnt+=1
            else:
                chars[dx]=chars[i-1]
                dx+=1
                if cnt>1:
                    for el in str(cnt):
                        chars[dx]=el
                        dx+=1
                cnt=1
        while len(chars) > dx:
            chars.pop()
        return dx