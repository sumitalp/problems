// Selection Sort

function selectionSort(array) {
  const swap = (x, y, arr) => {
		const temp = arr[x];
		arr[x] = arr[y];
		arr[y] = temp;
	}
	
	for(let i=0; i<array.length-1; i++){
		let minIndex = i;
		for(let j=i+1; j<array.length; j++){
			if(array[minIndex]>array[j]){
				minIndex = j;
			}
		}
		swap(i, minIndex, array);
	}
	
	return array;
}

// Do not edit the line below.
exports.selectionSort = selectionSort;

