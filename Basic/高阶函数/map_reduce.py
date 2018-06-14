from functools import reduce

def con(x,y):
    return x + y

li = [1,3,5,7]

l = map(str, li)

print(list(l))

summ = reduce(con, li)
print(summ)