listwl = [31,28,31,30,31,30,31,31,30,31,30,31]
listl = [31,29,31,30,31,30,31,31,30,31,30,31]
o = [7,1,2,3,4,5,6]
def l(x):
  k = 0
  if (x%4 == 0) and (x%100 != 0 or x%400 == 0) :
    k = 1
    return k
  else :
    return k
def f(x):
  nd = 0
  for i in range(x-1):
    nd = nd + listwl[i]
  return nd
def g(x):
  nd = 0
  for i in range(x-1):
    nd = nd + listl[i]
  return nd
date = int(input("Enter the date"))
month = int(input("Enter the month"))
year = int(input("Enter the year"))
d = 4
c = 0 
if year > 2026:
    for i in range (2026,year):
        if l(i) == 1 :
            c = c+2
        elif l(i) == 0:
            c = c+1
    c = c%7
    nn = 7-c
    e = o[d-nn]
elif year <=2026:
    for i in range(year,2026):
        if l(i) == 1 :
            c = c+2
        elif l(i) == 0:
            c = c+1
    c = c%7
    e = o[d-c]
    
    
if l(year) == 0:
  nd = f(month) + date
  m = nd % 7
  m = 7-m
  d = o[e-m-1]
  
  
elif l(year) == 1:
  nd = g(month) + date
  m = nd%7
  m = 7-m
  d = o[e-m-1]
  
if d == 1:
    print("Monday")
elif d == 2:
    print("Tuesday")
elif d == 3:
    print("Wednesday")
elif d == 4:
    print("Thursday")
elif d == 5:
    print("Friday")
elif d == 6:
    print("Saturday")
elif d == 7:
    print("Sunday")