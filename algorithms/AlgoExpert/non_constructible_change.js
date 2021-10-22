/*
  Non Constructible Change

  Given an array of positive integers representing the values of coins in your
  possession, write a function that returns the minimum amount of change (the
  minimum sum of money) that you cannot  create. The given coins can have
  any positive integer value and aren't necessarily unique (i.e., you can have
  multiple coins of the same value).
*/

function nonConstructibleChange(coins) {
	coins.sort((a,b) => a-b);

	let change = 0;
	for(const coin of coins){
		if(coin > change + 1) return change + 1;
		change += coin;
	}
	return change + 1;
}
