/*
Find Closest In BST

		10
	       /  \
             5      15
           /   \   /   \
          2     5 13    22
        /           \
       1             14
*/

// Solution 1: DFS
function findClosestValueInBst(tree, target) {
  const helper = (tree, target, closest) => {
		if (!tree) return closest;
		
		if(Math.abs(target-closest) > Math.abs(target-tree.value)){
			closest = tree.value;
		}
		if(tree.value > target) return helper(tree.left, target, closest);
		else if(tree.value < target) return helper(tree.right, target, closest);
		return closest;
	}
	
	return helper(tree, target, tree.value);
}

// This is the class of the input tree. Do not edit.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Do not edit the line below.
exports.findClosestValueInBst = findClosestValueInBst;


// Solution 2: BFS
function findClosestValueInBst(tree, target) {
  const helper = (tree, target, closest) => {
		let curr = tree;
		while(curr !== null){
			if(Math.abs(target-closest) > Math.abs(target-curr.value)){
				closest = curr.value;
			}
			if(curr.value > target){
				curr = curr.left;
			}
			else if(curr.value < target){
				curr = curr.right;
			}
			else{
				break;
			}
		}
		
		
		return closest;
	}
	
	return helper(tree, target, tree.value);
}

findClosestValueInBst(tree, 12);
// Output: 13
