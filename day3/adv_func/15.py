def funcb(gen):
    def funcc():
        gen()
        print("decorated house")
    return funcc

def funca():
    print("plain house")

funca()
print("----")

funca = funcb(funca)

####
funca()
