class Sample:
	data = 100
	datax = 70

obja = Sample()
objb = Sample()

print(obja.data)
print(objb.data)

objb.data = 20
Sample.data = 33
print(obja.data)
print(objb.data)

objc = Sample()

print(obja.data)
print(objb.data)
print(objc.data)

