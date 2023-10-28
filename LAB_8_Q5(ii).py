n =int(input("s: "))
l1 =[]
l2 =[]
for i in range(n):
  l2.append(int(input()))
  
for i in l2:
  if i<0:
    l1.append(0)
  else:
    l1.append(i**2)
print(l1)