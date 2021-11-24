class unix:

    def cmd(self):
        print("great command line")

    def secure(self):
        print("security enhanced by rwx")

class linux(unix):

    def free(self):
        print("the kernel is free")

    def secure(self):
        super().secure()
        print("can add anti-spywares too")

objl = linux()
objl.secure()
