# Importing the library
import tensorflow as tf

# Initializing the input
x = tf.constant([[2, 3, 6], [4, 8, 15]])

# Printing the input
print('\n', 'x:', x)

# Calculating result
res = tf.expand_dims(x, axis=2)

# Printing the result
print('\n', 'res: ', res)

print('\n')
print(res[1][1])