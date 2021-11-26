// Solution-1
function nodeDepths(root) {
  let sum = 0;
	let temp = [[root, 0]];
	
	while(temp.length > 0){
		[tree, depth] = temp.pop();
		sum += depth;
		
		if(tree.left) temp.push([tree.left, depth+1])
		if(tree.right) temp.push([tree.right, depth+1])
	}
	return sum;
}

// Solution-2
function nodeDepths(root) {
  const helper = (root, depth) => {
			if(!root) return 0;
			return depth + helper(root.left, depth+1) + helper(root.right, depth+1);
	}
	return helper(root, 0);
}


// This is the class of the input binary tree.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Do not edit the line below.
exports.nodeDepths = nodeDepths;

