import tensorflow as tf
import os

# file = os.path.join(os.getcwd(), 'text')
#
# dataset = tf.data.TextLineDataset(file)
#
# dataset = dataset.map(lambda string: tf.string_split([string]).values)

l = [1, 2, 3, 4, 5, 6]
t = tf.constant(l)
print(t)
print(t.shape)

t = tf.expand_dims(t, 1)
print(t)
print(t.shape)

#ex = tf.expand_dims(l, )

dataset = tf.data.Dataset.from_tensor_slices(t)
dataset = dataset.map(lambda x: x*2)
for line in dataset:
    print(line)
print('\n')

dataset = dataset.shuffle(2)
for line in dataset:
    print(line)
print('\n')

dataset = dataset.batch(17)
for line in dataset:
    print(line)
