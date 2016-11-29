// LeetCode: Pow(x,n) problem

func myPow(x float64, n int) float64 {
    var result float64
    var temp_n int
    
    if x == 0 || x == 1 || n == 1{
        return x
    }    
    
    if x == -1{
        if n % 2 == 0{
            return 1
        } else {
            return -1
        }
    }
    
    if n == 0{
        return 1
    }
    
    if n < 0{
        return 1 / myPow(x, -n)
    }
    
    temp_n = n / 2
    result = myPow(x, temp_n)
    
    if n % 2 == 0{
        return result * result
    }
    
    return result * result * x
}
