class Queue: 
  def __init__(self): 
    self.queue = [] 

  def enqueue(self,element): 
    self.queue.append(element) 

  def dequeue(self): 
    if self.isEmpty(): 
      return self.size == 0 
    return self.queue.pop(0)

  def peek(self): 
    if self.isEmpty():
      return "Queue is empty" 
    return self.queue[0] 

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self): 
    return len(self.queue)

  # Creating a Queue
myQueue = Queue() 

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
myQueue.enqueue('D')

print("Queue: ", myQueue.queue) 
print("Peek: ", myQueue.peek()) 
print("Dequeue: ", myQueue.dequeue()) 
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ",myQueue.isEmpty())
print("Size: ", myQueue.size())
