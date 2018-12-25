from sys import getsizeof as size
lst=[24,12,57]
a=10
print(size(a))
print(size(lst[1]))
print(len(lst))
e=len(lst)*size(lst[0])
print(e)
siz_of_list_object=size(lst)
print(siz_of_list_object)
