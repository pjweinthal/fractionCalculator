##-Fraction Calculator
#imports
import math

# Part 1 Inputs and Validation
numerator: int = 0
denominator: int = 0
fracProp: bool = True
while numerator <= 0:
    numerator = int(input("Enter a numerator: Value must be greater than 0: "))
    if numerator > 0:
        break
    else:
        print("Please re-enter the numerator. Value must be greater than 0 ")
while denominator <= 0:
    denominator = int(input("Enter a denominator: Value must be greater than 0: "))
    if denominator > 0:
        break
    else:
        print("Please re-enter the denominator. Value must be greater than 0 ")
# Part 2 & 3 Greatest Common Divisor and Outer If/Else
GCD = math.gcd(numerator, denominator)
if numerator > denominator:
    fracProp = False
    print("{0}/{1} is an improper fraction.".format(numerator,denominator))
    # Part 5 Nested If/Else Statement Improper Reduction Check
    if GCD != 0 and GCD != 1:
        numerator = int(numerator/GCD)
        denominator = int(denominator/GCD)
        print("This improper fraction can be reduced to : {0}/{1}".format(numerator,denominator))
    else:
        print("This improper fraction cannot be reduced any further.")
    mixedBeginning = int(numerator /  denominator)
    mixedTop = int(numerator % denominator)
    if mixedTop == 0:
        print("The whole number is {0}".format(mixedBeginning))
    else:
        print("The mixed number is {0} and {1}/{2}".format(mixedBeginning,mixedTop,denominator))
elif numerator < denominator:
    fracProp = True
    print("{0}/{1} is a proper fraction.".format(numerator, denominator))
    # Part 4 Nested If/Else Statement Proper Reduction Check
    if GCD != 0:
        numerator = int(numerator/GCD)
        denominator = int(denominator/GCD)
        print("This proper fraction can be reduced to: {0}/{1}".format(numerator,denominator))
    else:
        print("This proper fraction cannot be reduced any further.")

