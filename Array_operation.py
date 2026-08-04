array=[23,45,78,98,56]
print(array)
#Traversing
for i in array:
    print("The elements in the array are (Traversal):")
    print(i) 
#Insersion
array.insert(3,88)
print("The elements in the array after insertion are:")
print(array) 

#Deletion
array.remove(56)
print("The elements in the array after deletion are:")
print(array)