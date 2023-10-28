n = int(input())
l1 =[]
for i in range(n):
  l1.append(float(input("E: ")))
print(l1)
for i in range(n):
  for j in range(n-i-1):
    if  l1[j]>l1[j+1]:
      l1[j],l1[j+1] = l1[j+1],l1[j]
print(l1)