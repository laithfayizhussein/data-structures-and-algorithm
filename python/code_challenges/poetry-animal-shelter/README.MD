## Challenge Summary
Write a function called fizz buzz tree

Arguments: k-ary tree
Return: new k-ary tree
Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard


## Approach & Efficiency
Ceate function called fizz_buzz_tree take k_aryTree as argument
create inside it another function called _walk take node as argument
check if the node has children ->
loop of the children and call the function again and put the children as argument
do all 3 and 5  checks inside the loop and change the value for the node if it is true
return the kAry_Tree
repace the 3 and 5 in fizz and buzz if note match with 3 , 5 num create string of them


## Big O :
Time--> O(n)
space--> O(1)
