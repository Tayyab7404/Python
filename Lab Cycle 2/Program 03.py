# Program 3:

rupee_1 = int(input("Enter number of 1 rupee coins available: "))
rupee_5 = int(input("Enter number of 5 rupee coins available: "))
amount = int(input("Enter amount to be paid: "))

if (rupee_1 + rupee_5*5) == amount:
    print("1 rupee coins needed = ",rupee_1,"\t5 rupee coins needed = ",rupee_5)

elif (rupee_1 + rupee_5*5) > amount:
    coins_5 = amount//5
    if coins_5>rupee_5:
        coins_5 = rupee_5
    coins_1 = amount - (coins_5*5)
    print("1 rupee coins needed = ",coins_1,"\t5 rupee coins needed = ",coins_5)

else:
    print(-1)
