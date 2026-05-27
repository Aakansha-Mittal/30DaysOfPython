'''

List: Ordered, mutable, allows duplicates, indexed.
Tuple: Ordered, immutable, allows duplicates, indexed.
Set: Unordered, mutable, does not allow duplicates, not indexed.
Dictionary: Ordered (Python 3.7+), mutable, stores key-value pairs, keys are unique.

Index - access by position, Order - Kept in same sequence in which you inserted them. 


'''

# Create - list() or [] 

list = list()
list2 = [1, 'one', 1.0, 1+1j]
print(list)
print(list2)
# print(list2[5]) - Index out of range

#Unpacking - *
lst = [1,2,3,4,5,6,7,8,9,10]
one, two, three, *rest, ten = lst
print(one, two, three, rest, ten)

#Slicing
print(lst[0:12])
print(lst[15:20])
print(lst[-5:-1])

print(1 in lst)
print(15 not in lst)

#Methods

print(lst.append(11))