def funca():
    print("plain house")

def funcb(gen):
    def funcc():
        gen()
        print("decorated house")
    return funcc


funca()
print("----")

funca = funcb(funca)
# funcx = funcc

funca()
