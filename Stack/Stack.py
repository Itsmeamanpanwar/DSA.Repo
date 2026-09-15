Stack = [] 

# Push 
Stack.append('A')
Stack.append('B')
Stack.append('C')
Stack.append('D')
print("Stack: ", Stack)

# Peek 
Top_Element = Stack[-1] 
print(Top_Element)

# POP 
Popped_Element = Stack.pop() 
print("Popped Element: ", Popped_Element) 

# Stack After Pop
print("Stack:" , Stack) 

#isEmpty 
isEmpty = not bool(Stack) 
print("is Empty: ", isEmpty) 

#Size 
print("Size: ", len(Stack))