# Notes on using list() object 

lst = list()

# append to list
lst.append("Hi")
print(lst)

# INSERTING into list given an index
# inserts an element into the index and shifts the existing item at that index
# to the right. If the given index doesn't exist (index is bigger than list index range),
# it appends the new item at the end of the list
print("INSERTING")
lst.insert(0, "Hello")
lst.insert(5, "Meow")
lst.insert(6, "Boo")
print(lst)

# DELETING item from list
print("DELETING")
del lst[0]
print(lst)

# .pop() removes the last item from the list and returns it
a = lst.pop()
print(lst, a)
# it can also be used to remove an item from any position in a list
# by passing an index
b = lst.pop(0)
print(lst, b)

# .remove() removes the passed item in the list
# throws ValueError if the passed item doesn't exist in the list
lst.remove("Meow")
print(lst)

# SORTING lists
print("SORTING")

# temporary sorting
lst = [2, 4, 3, 2, 3]
print(sorted(lst))
print(sorted(lst, reverse=True))
print(lst)

# permanent sorting
lst.sort()
print(lst)

# reverse a list
lst.reverse()
print(lst)