# inner function
def funca():
    print("in a")
    def funcb():
        print("in b")
    funcb()
    print("in a")
    return funcb

x = funca()
print("----")
x()
