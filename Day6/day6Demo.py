#TUPLES

tup = tuple()
print(tup)

tup1 = (1)
#INT TYPE
print(type(tup1))
#TO CREATE SINGLE ITEM TUPLE ADD COMMA
tup1 = (1,)
print(type(tup1))

tup1 = (1,2,3,4,5)
tup2 = (6,7,8,9)
print(id(tup1))
tup1 = tup1 + tup2
print(id(tup1))
print(tup1)

lst = list(tup1)
print(type(lst))
print(lst)

del tup1
#print(tup1)

print(tup2.count(4))
print(tup2.index(7))