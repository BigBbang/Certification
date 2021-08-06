#https://www.tensorflow.org/api_docs/python/tf/expand_dims
import tensorflow as tf

image = tf.ones([3, 2, 2], dtype=tf.int8)
print(image)
print(image.shape)
print('\n')

image = tf.expand_dims(image, axis=0)
print(image)
print('\n')
print(image.shape)
