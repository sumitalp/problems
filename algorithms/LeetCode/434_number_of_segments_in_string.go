/**
You are given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.



Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1
Example 3:

Input: s = "love live! mu'sic forever"
Output: 4
Example 4:

Input: s = ""
Output: 0
*/

import (
	"strings"
	"regexp"
)

func countSegments(s string) int {
	s = strings.Trim(s, " ")
	if s == "" {
		return 0
	}

	space := regexp.MustCompile(`\s+`)
	s = space.ReplaceAllString(s, " ")

	segments := strings.Split(s, " ")
	return len(segments)
}