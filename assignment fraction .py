import math

#define variables
A = 1
B = 1


A = input("Input Numerator:")
while(A<=0):
    A = input("Input Numerator:")



B = (input("Input Denominator:")
while(B<=0):
    B = input("Input Denominator:")



GCDRESULT = int(math.gcd(A,B))

FRACTION = A/B

if (FRACTION < 1): #if fraction is less than one then it is proper, if more then improper
    print("Proper Fraction")

    if GCDRESULT == 1: #if gcd is one then cannot reduce
        print("Cannot be reduced")
    else:
        REDUCED = int(A/GCDRESULT), "/", int(B/GCDRESULT) #Change to fraction form
        print("Reduced Form", REDUCED) #print reduced form as a fraction

elif (FRACTION > 1):
    print("Improper Fraction")

    if GCDRESULT == 1:
        print("Cannot be reduced")
    else:
        REDUCED = int(A/GCDRESULT), "/", int(B/GCDRESULT)
        print("Reduced Form", REDUCED)

    INTEGER = A//B #get integer in mixed number
    REMAINDER = A%B #get remainder for numerator
    if (REMAINDER == 0):
        print("Mixed Number Form", INTEGER) #print mixed number form if remainder is 0
    else:
        print("Mixed Number Form", INTEGER," ", REMAINDER, "/", B) #print mixed number form