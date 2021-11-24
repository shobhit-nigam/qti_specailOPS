class Sample:
    x = 100
    y = 200

    def funca(self, val):
        self.x = val

    @classmethod
    def funcb(self, val):
        self.x = val

objs = Sample()

print(objs.x)
objs.funcb(11)
print(objs.x)

objt = Sample()
print(objt.x)
