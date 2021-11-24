class Sample:
    x = 100
    y = 200

    def funca(self, val):
        self.x = val

    @staticmethod
    def funcb():
        print("do nothing")

objs = Sample()
objs.funcb()
