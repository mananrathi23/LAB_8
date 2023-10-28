n= int(input())
l1 = []
for i in range(n):
  l1.append(int(input("E: ")))
print(l1)
max_no =None
for i in l1:
  if max_no == None or i>max_no:
    max_no = i 
print(max_no)