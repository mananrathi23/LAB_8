
# Online Python - IDE, Editor, Compiler, Interpreter

n = int(input("enter the number of test case :  "))
record = list()
for i in range(n):
  l = list()
  l.append(str(input("enter the name of student: ")))
  l.append(str(input("enter the roll no. of student: ")))
  l.append(float(input("enter the marks of the student: ")))
  record.append(l)
  record.sort()
  l2 = list()
  l2.append(f'rank{i} {record}')
print(l2)
