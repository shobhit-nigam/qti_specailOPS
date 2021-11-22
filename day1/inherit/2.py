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
print(isinstance(objl, linux))
print(isinstance(objl, unix))
print("----")
print(type(objl) == linux)
print(type(objl) == unix)
print("----")
print(type(objl) is linux)
print(type(objl) is unix)
