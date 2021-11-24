listb = [40, '', 'Hello', None, 0, 0.0, [], False, 60, [12, 13]]

print("listb =", listb)
listb = list(filter(None, listb))
print("listb =", listb)
