import  tensorflow as tf
import numpy as np
#
# t = tf.constant([[1, 2],
#                  [3, 4],
#                  [5, 6]], dtype=tf.int8)
#
# print('\n')
# print(t)
#
# print('\n')
# n = np.array(t)
# print(n)

a = tf.constant([1, 2, 3, 4])
print(a)
print(a.shape)

b = tf.expand_dims(a, axis=0)
print(b)
print(b.shape)


# c = tf.expand_dims(b, 2)
# print(c)