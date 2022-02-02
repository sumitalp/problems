/*
We need to ignore negative values from either sides or root node as well. However, if it has only one node with negative value then return it's value.
*/

function maxPathSum(tree) {
	const findMaxSum = (tree) => {
		if(!tree){
			return [0, -Infinity];
		}
		const [leftMaxSumAsBranch, leftMaxPathSum] = findMaxSum(tree.left);
		const [rightMaxSumAsBranch, rightMaxPathSum] = findMaxSum(tree.right);
		const maxChildSumAsBranch = Math.max(leftMaxSumAsBranch, rightMaxSumAsBranch);
		
		const maxSumAsBranch = Math.max(maxChildSumAsBranch + tree.value, tree.value);
		const maxSumAsRootNode = Math.max(maxSumAsBranch, leftMaxSumAsBranch + tree.value + rightMaxSumAsBranch);
		const maxPathSum = Math.max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode);
	
		return [maxSumAsBranch, maxPathSum];
	}
  
	const [_, maxSum] = findMaxSum(tree);
	return maxSum;
}

// Do not edit the line below.
exports.maxPathSum = maxPathSum;

