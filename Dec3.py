"""
This is the multiline comments
"""
# This is singleline comment
print("Hello")

def FirstFunction():
    print("Hello Again")

FirstFunction()

def ReturnSomething(parameter):
    print(parameter)
    return parameter

print(ReturnSomething(3))

def add(a,b):
    return a+b
print(add(2,4))


def sub(c,d):
    print(c)
    print(d)
    # Perform c - d
    return(c-d)

print (sub(6,8))
