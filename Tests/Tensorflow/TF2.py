# Importing the library
import tensorflow as tf

# Initializing the input
x = tf.constant([[2, 3, 6], [4, 8, 15]])

# Printing the input
print('x:', x)

# Calculating result
res = tf.expand_dims(x, 0)

# Printing the result
print('res: ', res)