n = int(input("Enter Size of Array: "))
array = []
hash = [0] * 51

for i in range(0, n):
    array.append(int(input("Insert Number into Array: ")))
    hash[array[i]] = hash[array[i]] + 1

q = int(input("Insert number of Querries: "))

for i in range(0, q):
    query = int(input("Insert Querry: "))
    count = hash[query]
    print(count)

# Optimize and reduce the time complexity by using hashing concept. 
# Time complexity is O(N+Q) which is much less than and better than O(N*Q).
# Space Complexity :- O(maximum number in the original array) = O(50) = size of the hash array. 
