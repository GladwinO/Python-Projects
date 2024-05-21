L = [0,1,2,3]
#L[4] #: This will return an error for indexing out of range
print(L[-1000:1000]) # when slicing out of bound and error is not returned and the entire list is returned, it is the same as L[:]

print(L[3:1]) #this returns an empty list
L[3:1] = ['?'] #it seems like the code disregards any number less than the starting number and assumes that the end postion is the starting number
print(L)
L[3:3] = ['x']
print(L)