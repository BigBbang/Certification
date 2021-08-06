#https://www.tensorflow.org/api_docs/python/tf/data/Dataset
import tensorflow as tf

# # using tf.data.Dataset.from_tensor_slices() method
# gfg = tf.data.Dataset.from_tensor_slices([[1, 2,], [3, 4]])
#
# for ele in gfg:
#     print(ele.numpy())

l = [1, 2, 3, 4, 5, 6]

ds = tf.data.Dataset.from_tensor_slices(l)
for i in ds:
    print(i)
#    tf.print(i)
print('\n')
print(list(ds.as_numpy_iterator()))
print('\n')

ds = ds.window(2, shift=1)
for i in ds:
    print(list(i))


print('\n')

# ds = ds.flat_map(lambda w: w.batch(2 + 1))
# for i in ds:
#     print(i)