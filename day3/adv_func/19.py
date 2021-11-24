def star(gen):
    def inner(*args):
        print("******")
        gen(*args)
        print("******")
    return inner

def hash(gen, generic):
    def inner(*args):
        print("#######")
        gen(*args)
        generic
        print("#######")
    return inner

@star
@hash
def display(statement):
    print(statement)


# display = star(hash(display))
