# Program 9:

def create_largest_number(L):
    L.sort(reverse = True)
    max = ''
    for n in L:
        max += str(n)
    return int(max)

L = [int(n) for n in input("Enter the numbers: ").split()]

print(f"The largest number possible from the given numbers is: {create_largest_number(L)}")
