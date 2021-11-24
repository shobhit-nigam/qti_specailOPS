class sample:
    ca = 100
    cb = 40

    def funca():
        la = 33
        lb = 44
        return dir()

objs = sample()
print(dir(objs))
print("---")
print(sample.__dict__)
