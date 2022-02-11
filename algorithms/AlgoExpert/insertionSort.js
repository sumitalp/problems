/**
Insertion sort

a = [2,7,5,1]
First iter (from index 1 to length of array):
  [2,7,5,1]
Second iter (from index 2 to length of array):
  [2,5,7,1]
Third iter (from index 3 to length of array):
  [2,5,1,7]
......
*/

function insertionSort(array) {
  for(let i=1; i<array.length; i++){
		let j = i;
		while(j>0 && array[j]<array[j-1]){
			const temp = array[j];
			array[j] = array[j-1];
			array[j-1] = temp;
			
			j--;
		}
	}
	
	return array;
}

// Do not edit the line below.
exports.insertionSort = insertionSort;

