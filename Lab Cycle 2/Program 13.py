# Program 13:

s1 = input("Enter first sentence: ")
s2 = input("Enter second sentence: ")

s = ""

for i in min(s1,s2):
    if i in max(s1,s2) and i != " ":
        s += i

if len(s) == 0:
    print(-1)
    
else:
    print(s)
