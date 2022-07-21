# Notes on using list() object 

lst = list()

# append to list
lst.append("Hi")
print(lst)

# inserting into list given an index
# inserts an element into the index and shifts the existing item at that index
# to the right. If the given index doesn't exist (index is bigger than list index range),
# it appends the new item at the end of the list
lst.insert(0, "Hello")
lst.insert(5, "Meow")
lst.insert(6, "Boo")
print(lst)

# deleting item from list
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

