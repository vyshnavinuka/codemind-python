number = int(input())
square = pow(number, 2)
mod = pow(10, len(str(number)))
if square % mod == number:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")