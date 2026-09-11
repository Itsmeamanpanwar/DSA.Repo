from collections import defaultdict

n = int(input("Enter Size of Array: "))
array = []
hash_map = defaultdict(int)

for i in range(0, n):
    num = int(input("Enter number in Array: "))
    array.append(num)
    hash_map[num] += 1

q = int(input("Enter number of Querries: "))

for i in range(0, q):
    query = int(input("Enter Querry: "))
    count = hash_map[query]
    print(count)

# TC :- O(N+Q) :- Insertion operation in a Hashmap has average O(1) time complexity and printing hashmap[i] also takes O(1) time on average. 
'''
Final Solution:- Use HashMap instead of Hash array (Key,Value) Pair Mapping 

Use HashMap Data structure!

It is exactly the same as Hashing array but it saves space! 

Hashmap only takes O(N) space in the worst case! Whereas Hashing array takes O(max element in array space)
'''