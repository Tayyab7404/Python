# Program 1:

A = int(input("Enter number of Adults: ")) 
C = int(input("Enter number of Children: "))

cost = A * 37550 + C * (37550/3) # Actual amount
cost += (0.07 * cost) # Service Tax = 7%
cost -= (0.1 * cost) # Discount = 10%

print("Total Ticket cost = ",cost)
