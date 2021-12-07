/*
Sample Input:
array = [2, 1, 2,2,2,3,4,2]
toMove = 2

Output:
[1,3,4,2,2,2,2,2]
*/

function moveElementToEnd(array, toMove) {
	let firstIdx = 0;
	let lastIdx = array.length - 1;
  
	while (firstIdx < lastIdx){
		if (array[firstIdx] !== toMove){
			firstIdx++;
		} else if(array[lastIdx] === toMove){
			lastIdx--;
		} else {
			if (array[firstIdx] === toMove){
				const temp = array[firstIdx];
				array[firstIdx] = array[lastIdx];
				array[lastIdx] = temp;
				firstIdx++;
			} else if(array[lastIdx] === toMove) {
				lastIdx--;
			}
		}
	}
	
	return array;
}

// Do not edit the line below.
exports.moveElementToEnd = moveElementToEnd;

