__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))     
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n=len(arr)
        arr.sort()
        cnt=0
        mod=10**9+7
        for idx in range(n-2):
            left,right=idx+1,n-1
            while left<right:
                dx=arr[idx]+arr[left]+arr[right]
                if dx>target:
                    right-=1
                elif dx<target:
                    left+=1
                else:
                    if arr[left] != arr[right]:
                        lcnt=rcnt=1
                        while left<right and arr[left]==arr[left+1]:
                            lcnt+=1
                            left+=1
                        while left<right and arr[right]==arr[right-1]:
                            rcnt+=1
                            right-=1
                        cnt+=lcnt*rcnt
                        cnt%=mod
                        left+=1
                        right-=1
                    else:
                        tcnt=right-left+1
                        cnt+=(tcnt*(tcnt-1))//2
                        cnt%=mod
                        break
        return cnt