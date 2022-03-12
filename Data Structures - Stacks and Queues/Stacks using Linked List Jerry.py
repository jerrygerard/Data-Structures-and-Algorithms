class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0
    
  def peek(self):
    return self.top.data

  def push(self,data):
    new_node = Node(data)
    if self.bottom == None:  # empty stack
      self.bottom = new_node
      self.top = self.bottom
      self.length = 1
    else:
      new_node.next = self.top # wire the new item to the current top
      self.top = new_node # make the new guy the new top
      self.length += 1

  def pop(self):
    if not self.top: #empty
      return None

    pop_value = self.top # grab the one we're popping
    self.top = self.top.next # set "top" to the item prior. next goes the other way here .. ?
    self.length -= 1
    return pop_value
    



  def pprint(self):
    temp = self.bottom

    print('bottom: ' + str(self.bottom.data))
    
    while temp != None:
      print('data: ' + str(temp.data))
  
      if temp.next == None:
        print('--> next: null')
        print('top: ' + str(temp.data))
      else:
        print('--> next: ' + str(temp.next.data))
      
      temp = temp.next
    
    print()
    print('Length = ' + str(self.length))

 

mystack = Stack()

mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')

print(mystack.peek())
 
mystack.pop()
mystack.pop()
mystack.pop() 

mystack.pprint()

