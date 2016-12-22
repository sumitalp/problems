// LeetCode: Longest Palindromic substring

// Solution with Manacher's Algorithm
// Code complexity: Big O n square
// Space complexity: Linear


package main

import "fmt"

func longestPalindrome(s string) string {
    sol := s[:1]
    
    for i:=0; i<len(s); i++{
        temp := findPalindorme(s, i, true)
        if len(temp) > len(sol) {
            sol = temp
        }
    }
    
    for i:=0; i<len(s); i++{
        temp := findPalindorme(s, i, false)
        if len(temp) > len(sol) {
            sol = temp
        }
    }
    
    return sol
}

func findPalindorme(s string, center int, isCenter bool) string {
    begin := 0
    end := 0
    
    if isCenter {
        begin = center
        end = center
    } else {
        begin = center
        end = center - 1
    }
    
    for begin > 0 && end < len(s)-1 && s[begin-1] == s[end+1] {
        begin--
        end++
    }
    //fmt.Println(begin, end)    
    return s[begin:end+1]
}

func main(){
	str := "babad"
	fmt.Println(longestPalindrome(str))
}
