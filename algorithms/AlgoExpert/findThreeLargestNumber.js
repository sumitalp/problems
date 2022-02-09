/**

Find Three Largest Number

Difficulty: Category: HiddenSuccessful Submissions: 41,949+Find Three Largest Numbers
Write a function that takes in an array of at least three integers and,
without sorting the input array, returns a sorted array of the three largest
integers in the input array.
The function should return duplicate integers if necessary; for example, it
should return [10, 10, 12] for an input array of
[10, 5, 9, 10, 12].
Sample Input
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample Output
[18, 141, 541]
HintsHint 1
Can you keep track of the three largest numbers in an array as you traverse the input array?
Hint 2
Following the suggestion in Hint #1, try traversing the input array and updating the three largest numbers if necessary by shifting them accordingly.
Optimal Space & Time ComplexityO(n) time | O(1) space - where n is the length of the input array

*/

// Approach - 1
function findThreeLargestNumbers(array) {
	let indexList = new Array(3).fill(-1);
	let n = 2;
	let max = -Infinity;
	while(n>=0){
		for(let i=0; i<array.length; i++){
			if(!indexList.includes(i) && array[i] > max){
				max = array[i];
				indexList[n] = i;
			}
		}

		max = -Infinity;
		n -= 1;
	}
	
	return [array[indexList[0]], array[indexList[1]], array[indexList[2]]];
}



// Approach - 2
// Time: O(n), Space: O(1)

function findThreeLargestNumbers(array) {
  const threeLargest = [null, null, null];
	for(const num of array){
		updateLargest(threeLargest, num);
	}
	return threeLargest;
}

const updateLargest = (arr, num) => {
	if(arr[2] === null || num > arr[2]){
		shiftAndUpdate(arr, num, 2);
	} else if(arr[1] === null || num > arr[1]){
		shiftAndUpdate(arr, num, 1);
	} else if(arr[0] === null || num > arr[0]){
		shiftAndUpdate(arr, num, 0);
	}
}

const shiftAndUpdate = (arr, num, idx) => {
	for(let i=0; i<=idx; i++){
		if(i===idx){
			arr[i]=num;
		} else {
			arr[i] = arr[i+1];
		}
	}
}

// Do not edit the line below.
exports.findThreeLargestNumbers = findThreeLargestNumbers;

