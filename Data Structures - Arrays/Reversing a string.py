def reverse(stri):
  mylist=[]
  for i in range(len(stri)-1,-1,-1):
    mylist.append(stri[i])
  return ''.join(mylist)


def reverse2(stri):
  return stri[::-1]

def reverse3(stri):
  return ''.join(reversed(stri))


x=reverse3('I am theja') 
print(x)  

# or just stri[::-1]

