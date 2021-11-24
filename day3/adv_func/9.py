# inner function
def funca():
    print("in a")
    def funcb():
        print("in b")
    print("in a")

funca()
