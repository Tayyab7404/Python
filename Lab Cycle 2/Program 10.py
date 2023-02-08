# Program 10:

def RLE(s):
    RLEcode =''
    n = len(s)
    i = 0
    
    while i < n:
        count = 1
        while (i+1 < n and s[i] == s[i + 1]):
            count += 1
            i += 1
        i += 1
        RLEcode += str(count) + s[i - 1]
    return RLEcode

s = input("Enter the string: ")

print(f"RLE code for '{s}' is '{RLE(s)}'")
