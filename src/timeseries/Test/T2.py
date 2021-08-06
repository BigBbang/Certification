#https://www.educative.io/edpresso/what-is-the-numpy-where-method


import numpy as np

# # Indices where the array elements fulfill the given condition
# arr = np.array([1,3,5,7,11]) # creating an ndarray
#
# index_arr = np.where(arr < 6) #calling the where method
#
# print(index_arr)

# #An array of elements rather than indices:
# arr = np.array([1,3,5,7,11]) # creating an ndarray
#
# elements_arr = arr[np.where(arr < 6)]
#
# print(elements_arr)

#Multiple arguments
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)

transformed_arr = np.where(arr<5, arr*10, 0)

print(transformed_arr)