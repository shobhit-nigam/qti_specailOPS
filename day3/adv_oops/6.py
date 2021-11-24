from decorators import count_calls

@count_calls
def funca():
    print("hi")
