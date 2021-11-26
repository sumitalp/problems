// This is the class of the input root.
// Do not edit it.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function branchSums(root) {
	let sums = [];
 	 const helper = (root, currSum, sums) => {
		if(!root) return sums;
		
		currSum += root.value;
		if(!root.left && !root.right){
			sums.push(currSum);
			return
		}
		if(root.left) helper(root.left, currSum, sums);
		if(root.right) helper(root.right, currSum, sums);
	}
	helper(root, 0, sums);
	return sums;
}

// Do not edit the lines below.
exports.BinaryTree = BinaryTree;
exports.branchSums = branchSums;

