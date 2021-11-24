# higher order functions
rava = "rava"
choco = "choco"
kaju = "kaju"

def laddu(x):
    print(f"making {x} laddoos")

def barfi(x):
    print(f"making {x} barfi")


def make(gen, x):
    gen(x)


make(laddu, rava)
print("---")
make(barfi, choco)
