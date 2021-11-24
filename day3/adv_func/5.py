def funca(la=11, lb=22, *args, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)


print("---")
x = funca(100, "hello", 300, 400, 500 , [8, 9, 10], india="delhi", norway="oslo")
