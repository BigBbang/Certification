import numpy as np

app = []

list = [1, 2, 3, 4]
split = np.array_split(list, 2)
app.append(split)

array = np.array(app)


print(app)

print(array)



# arr = [np.array(np.random.randint(1,17) for _ in range(5))]
# arrays = [np.array(np.random.randint(1, 17)) for _ in range(10)]
#
# print(arrays)
#
# print(np.random.randint(1, 17))