import numpy as np 


#creating array 
arr = np.array([
    [1,3,4,5],
    [6,7,8,9],
    ['a','b','c','d'],
    ['e','f','g','h']
], dtype=object)

print("=============")
print(arr)
print("=============")


#array indexing 
print("=============")
print(arr[1][2])
print("=============")

#array inserting 
arr = np.insert(arr,0,[['x','y','z','e']],axis=0)
print("=============")
print(arr)
print("=============")

#array appending 
arr = np.append(arr,[['x','y','z','e']],axis=0)
print("=============")
print(arr)
print("=============")


#array deleting 
arr = np.delete(arr,0,axis=0)
print("=============")
print(arr)
print("=============")
