# inner function
def funca():
    print("in a")
    def funcb():
        print("in b")
    funcb()
    print("in a")

funca()
# error
funcb()
