/*
Sample Input: 
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Output: [28, 26]
*/

// Time: [O(nlogn) + O(mlogm)], Space: O(1)  
function smallestDifference(arrayOne, arrayTwo) {
  arrayOne.sort((a, b) => a - b);
	arrayTwo.sort((a, b) => a - b);

	let aOneIdx = 0;
	let aTwoIdx = 0;
	let smallest = Infinity;
	let current = Infinity;
	let smallestPair = [];
	
	while(aOneIdx < arrayOne.length && aTwoIdx < arrayTwo.length){
		let aOneNum = arrayOne[aOneIdx];
		let aTwoNum = arrayTwo[aTwoIdx];

		if (aOneNum < aTwoNum){
			current = aTwoNum - aOneNum;
			aOneIdx++;
		} else if (aOneNum > aTwoNum){
			current = aOneNum - aTwoNum;
			aTwoIdx++;
		} else {
			return [aOneNum, aTwoNum];
		}
		
		if (current < smallest){
			smallest = current;
			smallestPair = [aOneNum, aTwoNum];
		}
	}

	return smallestPair;
}

