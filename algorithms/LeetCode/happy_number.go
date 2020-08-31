// Concept from Loop in linklist
// https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
package main

import "fmt"


func isHappy(n int) bool {
    // initialize slow  
    // and fast by n 
    slow := n; 
    fast := n; 
    for {
        // move slow number 
        // by one iteration 
        slow = numSquareSum(slow); 
  
        // move fast number 
        // by two iteration 
        fast = numSquareSum(numSquareSum(fast)); 
        if(slow != fast){
            continue;
        } else {
            break;
        }
    }
    
    // if both number meet at 1,  
    // then return true 
    return (slow == 1); 
}

func numSquareSum(n int) int {
    squareSum := 0
    m := n
    for m>0 {
        squareSum += (m%10) * (m%10)
        m = int(m/10) 
    }
    
    return squareSum
}

func main(){
	fmt.Println("Is 19 a happy number? ")
	fmt.Println(isHappy(19))

	fmt.Println("Is 20 a happy number? ")
	fmt.Println(isHappy(20))
}