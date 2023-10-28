n = int(input())
l1 =[]
l2 = []
for i in range(n):
  l1.append(float(input("E: ")))
print(l1)
for i  in range(n):
  x = min(l1)
  l2.append(x)
  l1.remove(x)
print(l2)