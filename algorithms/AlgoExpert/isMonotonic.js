/*
  Write a function that takes in an array of integers and returns a boolean
  representing whether the array is monotonic.

  An array is said to be monotonic if its elements, from left to right, are
  entirely non-increasing or entirely non-decreasing.

  Non-increasing elements aren't necessarily exclusively decreasing; they simply
  don't increase. Similarly, non-decreasing elements aren't necessarily
  exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

Sample Input:
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output: true

Approach:
1. Find if it is non increasing.
2. Find if it is non decreasing.
3. Then return either both cases found.
*/


function isMonotonic(array) {
  let nonIncr = true;
	let nonDecr = true;
	
	for(let i=1; i<array.length; i++){
		if (array[i-1] > array[i]) nonDecr = false;
		if (array[i-1] < array[i]) nonIncr = false;
	}
	
	return nonIncr || nonDecr;
}

// Do not edit the line below.
exports.isMonotonic = isMonotonic;

