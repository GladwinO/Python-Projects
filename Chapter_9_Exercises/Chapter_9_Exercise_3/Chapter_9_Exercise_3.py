L = [3, 345, 5, 56]; print(L)
L[2] = []; print(L, end = '\n\n')

L[2:3] = []; print(L, end = '\n\n')

del L[0]; print(L)
del L[1:]; print(L, end = '\n\n')


L[1:2] = 1; print(L)#Error received: TypeError: can only assign an iterable. I assume since I am slicing through a list instead of 
#assigning at one position I would need a sequence as a replacement and not just an int

# this code and below will not run because of the error that occurs above
L[1:2] = [1,2,3]; print(L)
L[2] = 1; print(L) 
