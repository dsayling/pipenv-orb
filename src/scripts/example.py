
import os

def test_func(x,y):
    addition = x+y
    print(addition)
    return addition

if __name__ == "__main__":
    ## Access the envvars set in the command
    x = os.getenv("PARAM1")
    y = os.getenv("PARAM2")
    test_func(x,y)