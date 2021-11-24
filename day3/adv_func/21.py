def star(gen):
    def inner(*args):
        print("******")
        gen(*args)
        print("******")
    return inner

@star
def hash(gen, generic):
    def inner(*args):
        print("#######")
        gen(*args)
        generic(*args)
        print("#######")
    return inner


@hash
def display(statement):
    print(statement)

@hash
def show(statement):
    print(statement)
