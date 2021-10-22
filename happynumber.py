class Solution:
    def isHappy(self, n: int) -> bool:
        s=0
        if n<10:
            if n==1 or n==7:
                return 1
            else:
                return 0
        else:
            while n!=0:
                r=n%10
                n=n//10
                s=s+pow(r,2)
            return self.isHappy(s)
        
