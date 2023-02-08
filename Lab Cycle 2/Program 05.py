# Program 5:

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

L = []

if num1<num2:
    for i in range(num1, num2+1):
        if len(str(i)) == 2:
            if i%5 == 0:
                if (i//10 + i%10) % 3 == 0:
                    L.append(i)

if len(L)==0:
    print(-1)
else:
    print(max(L))
