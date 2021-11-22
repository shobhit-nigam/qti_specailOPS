# multiple and multilevel

class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("security enhanced by rwx")

class linux(unix):
    def free(self):
        print("the kernel is free")

class mobileOS:
    def portable(self):
        print("can be ported to various devices")

    def free(self):
        print("the os is free")

class android(mobileOS, linux):
    def ui(self):
        print("great ui")

obju = unix()
objl = linux()
obja = android()

obja.free()
