#remove duplicates

a = ('John John Zizi Zizi Ali Ali')

b = a.split()

newa = []
for x in b:
   if x not in newa:
      newa.append(x)
print(newa)



