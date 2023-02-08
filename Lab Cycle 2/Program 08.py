# Program 8:

def isLeapYear(y):
    if (y%400 == 0) or (y%4 == 0 and y%100 != 0):
        return True
    return False

y = int(input("Enter the starting year: "))

n = y

LeapYears = []

while len(LeapYears) < 15:
    if isLeapYear(y+1):
        LeapYears.append(y+1)
    y += 1

print(f"The first 15 leap years from {n} are {LeapYears}")
