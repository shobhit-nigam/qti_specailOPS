class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("security enhanced by rwx")

class linux(unix):
    def free(self):
        print("the kernel is free")



obju = unix()
objl = linux()
objl.secure()
