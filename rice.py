print("1.")

for i in range(0,4):       
    for b in range(0,7):
        print("*",end="")
    print()

print("2.")

#自解
for x in range(1,8,2):
    print("*"*x)
print()
#雙重
for i in range(1,8,2):
    for b in range(i):
        print("*",end="")
    print()

print("3.")

for i in range(1,10,2):
    for b in range(i):
        print("*",end="")
    print()
for i in range(7,0,-2):
    for b in range(i):
        print("*",end="")
    print()