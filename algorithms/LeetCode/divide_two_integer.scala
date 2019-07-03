// Leetcode 29. Divide Two Integer

object Solution {
    def divide(dividend: Int, divisor: Int): Int = {
        var p:Int = dividend.abs
        var q:Int = divisor.abs
        
        var ret: Int = 0;
        while (p >= q) {
            var counter:Int = 0;
            while (p >= (q << counter)) {
                counter+=1;
            }
            ret = ret + (1 << (counter - 1));
            p = p - (q << (counter - 1));
        }

        if (dividend == Int.MinValue && divisor == -1)
            return Int.MaxValue;
        
        if ((dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0))
            return ret;
        else
            return -ret;
    }
}

// Solution above failed "Time Limit Exceeded for divide(2147483647, 1)", it's mean when divisor is too low
