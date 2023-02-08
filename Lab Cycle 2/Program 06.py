# Program 6:

L = [int(x) for x in input("Enter the elements: ").split()]

count = 0

for i in range(len(L)-1):
    if L[i] == L[i+1]:
        count += 1

print(count)
