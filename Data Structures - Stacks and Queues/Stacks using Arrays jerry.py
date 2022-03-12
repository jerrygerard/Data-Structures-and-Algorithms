class Stack:
  def __init__(self):
    self.arr = [] 
  
  def __str__(self):
    return str(self.__dict__)
  
  def peek(self):
    return self.arr[-1]

  def push(self,value):
    self.arr.append(value)

  def pop(self):
    popped_item = self.arr.pop()
    return popped_item

mystack = Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
print(mystack)
x = mystack.peek()
print(x)
mystack.pop()
print(mystack)


