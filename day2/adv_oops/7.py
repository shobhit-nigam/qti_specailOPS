class sample:
    ca = 100
    __cb = 40

    def funca():
        la = 33
        lb = 44
        return dir()

    def __dir__(self):
        return ['ca', 'funca']

objs = sample()
print(dir(objs))
