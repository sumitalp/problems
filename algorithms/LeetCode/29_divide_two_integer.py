class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        p = abs(dividend)
        q = abs(divisor)
        ret = 0
        signed = -1 if (dividend<0 and divisor>0) or (dividend>0 and divisor<0) else 1

        if q > 1:
            while p>=q:
                counter = 0
                while p >= (q<<counter):
                    counter +=1

                ret = ret + (1<<(counter-1))
                p = p - (q << (counter-1))
        else:
            ret = p
            
        ret = ret * signed
            
        min_int = -2**31
        max_int = (min_int*-1) - 1
        
        if ret > max_int:
            ret = max_int
        if ret < min_int:
            ret = min_int
        
        return ret

if __name__=='__main__':
	print(Solution().divide(2**31-1, 2))
