class Bank:
    def __init__(self, accnum, opbal):
        self.accnum = accnum
        self.opbal = opbal

    def __bool__(self):
        if self.accnum < 1:
            return False
        else:
            return True

objs = Bank(23568, 1000)
objt = Bank(0, 2000)

if objs:
    print("objs exists")
else:
    print("objs does not exist")


if objt:
    print("objt exists")
else:
    print("objt does not exist")
