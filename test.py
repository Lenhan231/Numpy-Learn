n = 1234
n = str(n)
ls = []
for i in range(len(n)):
    ls.append(n[0:len(n) - i])
print(ls)