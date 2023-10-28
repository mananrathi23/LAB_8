n =int(input())
l1= []
l2= []
for i in range(n):
  l1.append(int(input("E: ")))

for i in l1:
  if i<20 and i>10:
    l2.append(i**2)
  else:
    l2.append(i)
print(l2)