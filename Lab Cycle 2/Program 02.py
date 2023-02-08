# Program 2:

a = []

while len(a) != 3:
    a = [int(x) for x in input("Enter three numbers: ").split()]

if 7 in a:
    if a.index(7)==0:
        ans = a[1]*a[2]
    elif a.index(7)==1:
        ans = a[2]
    else:
        ans = -1

else:
    ans = a[0]*a[1]*a[2]

print(ans)
