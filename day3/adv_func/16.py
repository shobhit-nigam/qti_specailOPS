def funcb(gen):
    def funcc():
        gen()
        print("decorated house")
    return funcc

@funcb
def funca():
    print("plain house")


#funca = funcb(funca)
# funca = funcc

funca()
