n = 8

#--------------------------------------------#

print("Maximize")
s = ""
f= True
for x in range(ord('a'), ord('a') + n):
    for y in range(1, n+1):
        if f:
            s += (chr(x) + str(y))
            f = False
        else:
            s += ("+" +chr(x) + str(y))
print(str(s))
print()

#--------------------------------------------#

print("Subject To")
s = ""
f = True

for x in range(ord('a'), ord('a')+n):
    for y in range(1, n+1):
      if y == n:
          s += (chr(x) + str(y) + "<=1")
      else:
          s += (chr(x) + str(y) + "+")
    print(s)
    s = ""

for i in range(2, n):
    for k in range(1, i+1):
        s += (chr(ord('a') + n-i+k-1) + str(k))
        if k == i:
            s += ("<=1")
        else:
            s += ('+')
    print(s)
    s = ""

for y in range(1, n):
    s += (chr(ord('a') + y-1) + str(y) + "+")
s += (chr(ord('a') + n-1) + str(n) + "<=1")
print(s)
s = ""

for i in range(2, n):
    for k in range(1, n-i+2):
        s += (chr(ord('a') + k-1) + str(k+i-1))
        if k == n-i+1:
            s += ("<=1")
        else:
            s += ('+')
    print(s)
    s = ""

for y in range(1, n+1):
    for x in range(ord('a'), ord('a')+n):
        if x == (ord('a') + n - 1):
            s += (chr(x) + str(y) + "<=1")
        else:
            s += (chr(x) + str(y) + "+")
    print(s)
    s = ""

for i in range(2, n):
    for k in range(1, i+1):
        s += (chr(ord('a') + k-1) + str(i-k+1))
        if k == i:
            s += ("<=1")
        else:
            s += ('+')
    print(s)
    s = ""

for y in range(1, n):
    s += (chr(ord('a') + y-1) + str(n+1-y) + "+")
s += (chr(ord('a') + n-1) + str(1) + "<=1")
print(s)
s = ""

for i in range(2, n):
    for k in range(1, n-i+2):
        s += (chr(ord('a') + k+i-2) + str(n-k+1))
        if k == n-i+1:
            s += ("<=1")
        else:
            s += ('+')
    print(s)
    s = ""

print()

#--------------------------------------------#

print("Bounds")
for x in range(ord('a'), ord('a')+n):
    for y in range(1, n+1):
        print("0<=" + chr(x) + str(y) + "<=1")
print()

#--------------------------------------------#

print("Generals")
for x in range(ord('a'), ord('a')+n):
    for y in range (1, n+1):
        print(chr(x)+str(y))
print()

#--------------------------------------------#

print("End")