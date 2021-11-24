def hash(gen):
    def inner(*args):
        print("#######")
        gen(*args)
        print("#######")
    return inner

@hash
def display(statement):
    print(statement)

# display = hash(display)
# display = inner


display("hello world")
