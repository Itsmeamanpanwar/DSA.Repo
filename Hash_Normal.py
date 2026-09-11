n = int(input("Enter length of array: "))
array = list(map(int,input("Array: ").split())) 

q = int(input("Number of Query to run: "))

for i in range(0, q):
    query = int(input("Querry: "))
    
    count = 0
    for j in range(0, n):
        if array[j] == query:
            count += 1
    print(count)


# Complexity : Time Complexity :- O(N + N*Q) = O(N*(1+Q)) ====O(N*Q) 
#             Space Complexity :- Took O(1) size
