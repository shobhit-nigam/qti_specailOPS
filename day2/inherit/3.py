class unix:
    def __init__(self):
        print("init of unix")

    def cmd(self):
        print("great command line")

    def secure(self):
        print("security enhanced by rwx")

class linux(unix):
    def __init__(self):
        super().__init__()
        print("init of linux")

    def free(self):
        print("the kernel is free")

    def secure(self):
        print("rwx makes t secure, can add anti-spywares too")

obju = unix()
print("---")
objl = linux()
