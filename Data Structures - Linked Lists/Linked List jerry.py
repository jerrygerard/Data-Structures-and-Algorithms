# 15 --> 6 --> 8

class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
  
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
      self.tail = new_node
      self.length += 1

  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head # wire the new one before the existing #1
    self.head = new_node

    self.length += 1
  
  def insert(self, index, data):
    new_node = Node(data)
    i = 0
    temp = self.head

    if index >= self.length:  # tack it on the end
      self.append(data)
      return

    if index == 0:  # stick in on the front
      self.prepend(data)
      return

    while i<self.length:
      if i == index - 1:  # find the spot
        temp.next, new_node.next = new_node, temp.next
        self.length += 1
        break
      temp = temp.next
      i += 1

  def remove(self, index):
    
    # initialize
    temp = self.head
    i = 0

    if index >= self.length:  #whoops
       print("Entered wrong index")

    if index == 0:
      self.head = self.head.next  # the second is now the first
      length -= 1
      return
    
    while i < self.length:
      if i == index - 1:
        temp.next = temp.next.next # wire around the deleted one
        self.length -= 1
        break

      i += 1
      temp = temp.next # go to the next one

  def printl(self):
    temp = self.head

    while temp != None:  # keep chugging til you hit the end
      print(temp.data, end = ' ')  
      temp = temp.next
    print()
    print('Length = ' + str(self.length))

  def pprint(self):
    temp = self.head

    while temp != None:
      print('data: ' + str(temp.data))
      
      if temp.next == None:
        print('--> next: null')
      else:
        print('--> next: ' + str(temp.next.data))
      
      temp = temp.next

    print()
    print('Length = ' + str(self.length))
    print()
    print('Head: ' + str(self.head.data))
    print('Tail: ' + str(self.tail.data))

    
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
l.reverse()

l.pprint()




