Hashtables
a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.



Challenge
Implement a Hashtable Class with the following methods:

add
get
contains
hash
Approach & Efficiency
add : time : O(n) space : O(1)

get : time : O(n) space : O(1)

contains: time: O(n) space: O(1)

hash: time: O(n) space: O(1)

API
add: This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

get: This method returns Value associated with that key in the table.

contains: This method returns Boolean, indicating if the key exists in the table already.

hash: This method returns Index in the collection for that key
