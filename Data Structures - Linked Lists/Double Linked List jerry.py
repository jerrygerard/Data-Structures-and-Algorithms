# 15 --> 6 --> 8

class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
  
class LinkedList():
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, data):
    new_node = Node(data) 
    if self.head == None:  # add the first thing 
      self.head = new_node
      self.tail = self.head 
      self.length = 1
    else:
      self.tail.next = new_node # tack it on and make it the new tail
      new_node.prev = self.tail
      self.tail = new_node
      self.length += 1

  def prepend(self, data):
    new_node = Node(data)
    self.head.prev = new_node
    new_node.next = self.head # wire the new one before the existing #1
    self.head = new_node

    self.length += 1

  def get(self, index):
    desired_node = self.traverseToIndex(index)
    return desired_node.data

  def traverseToIndex(self, index):
    counter = 0
    currentNode = self.head
    
    while counter != index:
      currentNode = currentNode.next
      counter += 1

    return currentNode
  
  def insert(self, index, data):
    new_node = Node(data)
    i = 0

    if index >= self.length:  # tack it on the end
      self.append(data)
      return

    if index == 0:  # stick in on the front
      self.prepend(data)
      return  

    leader = self.traverseToIndex(index - 1)
    temp = leader.next # existing value at that spot
    leader.next = new_node # new value
    new_node.next = temp
    new_node.prev = leader
    temp.prev = new_node
    
    self.length += 1
        
  def remove(self, index):
    
    # initialize
    temp = self.head
    i = 0

    if index >= self.length:  #whoops
       print("Entered wrong index")
       return

    if index == 0:
      self.head = self.head.next  # the second is now the first
      length -= 1
      return
    
    leader = self.traverseToIndex(index - 1)
    unwanted_node = leader.next # the one to kill
    after = unwanted_node.next
   
    if unwanted_node != self.tail:
      leader.next = unwanted_node.next # wire to the one after the dead one
      after.prev = leader
    else:
      leader.next = None
      self.tail = leader
   
    self.length -= 1    

  def printl(self):
    temp = self.head

    while temp != None:  # keep chugging til you hit the end
      print(temp.data, end = ' ')  
      temp = temp.next
    print()
    print('Length = ' + str(self.length))

  def pprint(self):
    temp = self.head

    print('Head: ' + str(self.head.data))
    print()

    while temp != None:
      if temp.prev == None:
        print('--> prev: null')
      else:
        print('--> prev: ' + str(temp.prev.data))
      
      print('data: ' + str(temp.data))
    
      if temp.next == None:
        print('--> next: null')
      else:
        print('--> next: ' + str(temp.next.data))
    
      print()
      temp = temp.next

    print('Tail: ' + str(self.tail.data))
    print()
    print('Length = ' + str(self.length))
   

  def reverse(self):
    prev = None
    self.tail = self.head

    while self.head != None:
      temp = self.head
      self.head = self.head.next
      temp.next = prev
      prev = temp
    self.head = temp


l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.prepend(1)
l.insert(2,99)
l.insert(34,23)
l.remove(5)
# l.reverse()

print(l.get(1))
print(l.get(3))

l.pprint()




