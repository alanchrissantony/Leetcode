class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        dx,dy=red,blue
        x,y=1,2
        zx=0
        while dx>=x and dy>=y:
            if dx>=x:
                dx-=x
                x+=2
                zx+=1

            if dy>=y:
                dy-=y
                y+=2
                zx+=1
            else:
                dx=0
        if dx>=x:
            zx+=1
        dx,dy=blue,red
        x,y=1,2
        zy=0
        while dx>=x and dy>=y:
            if dx>=x:
                dx-=x
                x+=2
                zy+=1

            if dy>=y:
                dy-=y
                y+=2
                zy+=1
            else:
                dx=0
        if dx>=x:
            zy+=1
        return (max(zx,zy))