count1,count2,count3,count4,count5 = 0,0,0,0,0
while True:
  n = int(input())
  if n == -1 :
    break 
  if n>=1 and n<=10:
    if n>=1 and n<=2:
      count1 += 1
    if n>=3 and n<=4:
      count2 +=1
    if n>=5 and n<=6:
      count3 +=1
    if n>=7 and n<=8:
      count4 +=1
    if n>=9 and n<=10:
      count5 +=1
total = count1+count2+count3+count4+count5
print("#"*count1 , end ="")
print(f'{(count1/total)*100:.2f}% ')
print("#"*count2 , end ="")
print(f'{(count2/total)*100:.2f}% ')
print("#"*count3 , end ="")
print(f'{(count3/total)*100:.2f}% ')
print("#"*count4 , end ="")
print(f'{(count4/total)*100:.2f}% ')
print("#"*count5 , end ="")
print(f'{(count5/total)*100:.2f}% ')