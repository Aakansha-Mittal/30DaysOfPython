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
print(len(lst))
one, two, three, *rest, ten = lst
print(one, two, three, rest, ten)

#Slicing
print(lst[0:3])
print(lst[0:12])
print(lst[15:20])
print(lst[-5:-1])

print(1 in lst)
print(15 not in lst)

#Modify
lst[0]=11
print(lst)

#Methods
#1. Append - Add at last an element or a list and return None.
#2. insert(index, item) - Insert single item or a list at specified index,
#  if index is large then insert at end, return none.
#3. remove(item) - remove specified item, return None, and if item is not present then error. 
#4. pop(index) - returns the deleted item, if index not present then error. Works with -ve index also.
#5. del <list>[]- delete item at specified index, or range or complete list. 
#6. clear() - empties the list.
#7. copy() - Creates a shallow copy, NEW OUTER OBJECT BUT NESTED OBJECTS ARE STILL SHARED.
#8. count(item) - returns frequency of item and if item is not there then, 0.
#9. <lst1>.extend(<lst2>) - add lst2 to lst1
#10. reverse() - reverse the list.
#11. sort() or sort(reverse=true) - sort and modifies the original list.
#12. sorted(<list>) - sort the passed list and returns the sorted list, don't modify the original one.


print(lst.append(11))
print(lst)
print(lst.append([12,13]))
print(lst)
print(list)
list.append([1, 'a'])
print(list)
print(lst.insert(12, 13))
print(lst)
print(lst.insert(12, [13, 14]))
print(lst)
print(lst.insert(20, ['a', 'b']))
print(lst)

print(lst.remove([12,13]))
print(lst)

print(lst.pop(-1))
print(lst)
print(lst.pop(2))
print(lst)
print(lst.pop())
print(lst)

print('del')
print(lst)
print('del 7')
del lst[7]
print(lst)
del lst[0:2]
print(lst)
del lst[:]
print(lst)
del lst
#print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.clear())
print(fruits) 


#COPYING THE LIST
'''
It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. 
Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. 
But there are lots of case in which we do not like to modify the original instead we like to have a 
different copy. One of way of avoiding the problem above is using copy().


'''

lst1 = [1,2,3,4,5, [1,2], [3,4]]
lst2 = lst1
print(lst1)
lst2.append(6)
lst2.remove(1)
print(lst2)
print(lst1)

lst2 = lst1.copy()
#This change will not be reflected into lst2.
lst2.append(6)
lst2[5][0] = 100
print(lst1)
print(lst2)

#DEEP COPY
import copy
lst1 = [1,2,[3,4],(5,6)]
lst2 = copy.deepcopy(lst1)
print(lst1 is lst2)
print(lst1[2] is lst2[2])

lst = [1,2,3,4,5,3,2,1,6]
print(lst.count(1))
print(lst.extend(lst2))
print(lst)