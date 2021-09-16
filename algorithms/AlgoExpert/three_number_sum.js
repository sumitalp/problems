// Time: O(n^2) | Space: O(n)
function threeNumberSum(array, targetSum) {
	array.sort((a,b) => a-b);
	let retResult = new Array();
	
	for(let i=0; i<array.length-2; i++){
		let leftIdx = i+1;
		let rightIdx = array.length - 1;

		while(leftIdx<rightIdx){
			const total = array[i]+array[leftIdx]+array[rightIdx];

			if(total===targetSum){
				retResult.push([array[i],array[leftIdx],array[rightIdx]]);
				leftIdx++;
				rightIdx--;
			} else if(total<targetSum){
				leftIdx++;
			} else if(total>targetSum) {
				rightIdx--;
			}
		}
	}
	
	return retResult
}

// Do not edit the line below.
exports.threeNumberSum = threeNumberSum;

