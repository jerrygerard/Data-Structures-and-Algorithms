def func(mylist):
  '''
  add each character to a hashtable "seen"
  as soon as we see one again, return it
  '''

  seen = []

  for i in range(len(mylist)):
    if mylist[i] in seen:
      return mylist[i]
    
    seen.append(mylist[i])

  return "none"



'''

  for i in range(0,len(mylist)):
    for j in range(i+1,len(mylist)):
      if mylist[i] == mylist[j]:
        return mylist[i] 
  return 0

def hashtable(mylist):
  mydict = {}
  for i in range(0,len(mylist)):
    if mylist[i] in mydict:
      return mylist[i]
    else:
      mydict[mylist[i]]=i
  return 0
  

'''
mylist = [2,1,2,3,4,5]
x = func(mylist)
print(x)
