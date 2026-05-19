'''
1. zip() in Python is used to combine multiple iterables (like lists, tuples, etc.) 
element-wise into pairs or groups.
2. It returns a zip object (iterator), so to see the output properly 
we usually convert it using list(), tuple(), dict(), etc.
3. By default, zip() works till the shortest iterable length (strict=False behavior),
so extra elements in longer iterables are ignored.
4. We can use strict=True in zip() to ensure all iterables have the same length;
otherwise Python raises a ValueError.
5. Common use cases include looping through multiple lists together, 
creating dictionaries, and pairing related data.
'''



#from itertools import zip_longest
import itertools

#shortest length as strict=False by default
print(list(zip('abcdefg', range(5), range(4))))

#strict=True so gives a ValueError as length of all args is not same. 
#print(list(zip('abcdefg', range(5), range(4), strict=True)))

#If we want that all values should be there ir respect of diff length of args. 
print(list(itertools.zip_longest('abcdefg', range(5), range(4))))

#fillValue with the passed arg
print(list(itertools.zip_longest('abcdefg', range(5), range(4), fillvalue='???')))
