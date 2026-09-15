queue = [] 

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
queue.append("D")
queue.append("E") 
print("Queue", queue)

#peek 
frontElement = queue[0]
print("Peek: ", frontElement) 

# Dequeue 
poppedElement = queue.pop(0) 
print("Dequeue: ", poppedElement) 

print("Queue after Dequeue: ", queue) 

# isEmpty 
isEmpty = not bool(queue) 
print("is Empty: ", isEmpty) 

#Size
print("Size: ", len(queue)) 


