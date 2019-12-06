# Pointing to the library
from mymath import *
print (add(2,4))

print (div(10,5))

# training on if/or
a = 5
# equal is ==
if a == 3 and a < 5:
    print ("this is impossible")

if a == 3:
    print ("a is 3")
elif a == 4:
    print ("a is 4")
# When there is third expression involved, use else
else:
    print ("Something Else")

# when you write if, elif, always include esle

def decision (age1, age2):
    result = (age1/2)+7
    if age2 < result:
        return ("too young")
    else:
        return ("Perfect")

# print (decision(45,18))

assert decision(45,18) == "too young" and decision(14,14) == "Perfect"
assert decision(95, 35) == "Perfect"
