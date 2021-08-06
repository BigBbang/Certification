import tensorflow as tf
import numpy as np
d = np.arange(0,60).reshape([6, 10])

data = tf.data.Dataset.from_tensor_slices(d)
for i in data:
    print(i)


print('\n')

data = data.shuffle(buffer_size=3)
for i in data:
    print(i)