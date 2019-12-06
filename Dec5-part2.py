from mymath import *

if __name__=="__main__":
    a = 5
    b = 2
    c = 10
# assert is used for testing
    assert add(a,b) == c , "this is wrong {} + {} should not equal {}".format(a,b,c)
