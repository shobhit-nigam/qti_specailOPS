dicta = {'aa':10, 'bb':20, 'cc':30, 'dd':40, 'ee':50}

dictb = {key:val for (key, val) in dicta.items() if val%20==0 }

print(dictb)
