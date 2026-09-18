# Creating a simple list.. 

list = [None, None, None, None, None, None, None, None, None, None] 

# Creating a hash function..
def hash_function(value): 
  sum_of_chars = 0 
  for char in value: 
    sum_of_chars += ord(char) 

  return sum_of_chars % 10 

print("Bob has hash funciton: ", hash_function('Bob'))

# Inserting an Element 
def add(name): 
  index = hash_function(name) 
  list[index] = name 

add('Bob') 
print(list)

add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(list)

# LOOKING UP A NAME 
def contains(name): 
  index = hash_function(name) 
  return list[index] == name 

print("'Pete' is in the Hash Table:", contains('Pete'))

