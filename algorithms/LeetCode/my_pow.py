class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==0:
            return 1
        
        MAX = 100000
        res = [0] * MAX
        res_size = 0
        negative_n = True if n < 0 else False
        negative_x = True if x < 0 and n%2!=0 else False
        n, x = abs(n), abs(x)
        temp = x
        
        while temp != 0:
            res[res_size] = temp % 10
            res_size += 1
            temp //= 10
        
        def multiply(x, res, res_size):
            # Initialize carry 
            carry = 0

            # One by one multiply n with 
            # individual digits of res[] 
            for i in range(res_size): 
                prod = res[i] * x + carry 

                # Store last digit of 
                # 'prod' in res[] 
                res[i] = prod % 10

                # Put rest in carry 
                carry = prod // 10

            # Put carry in res and 
            # increase result size 
            while (carry): 
                res[res_size] = carry % 10
                carry = carry // 10
                res_size+=1

            return res_size 
            
        
        for i in range(2, n+1):
            res_size = multiply(x, res, res_size)
            
        result = 0
        for j in range(len(res)-1, -1, -1):
            if isinstance(res[j], float):
                result += res[j] * 10**j
                
        if negative_n:
            result = 1/result
        result *= -1 if negative_x else 1
        return result

# Testcases
#2.00000
#10
#2.10000
#3
#2.00000
#-2
#-2.00000
#2
#-2.00000
#-2
#4.36852
#-2
