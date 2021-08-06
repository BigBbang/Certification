import numpy as np
import tensorflow as tf

DATA_URL = 'https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz'

path = tf.keras.utils.get_file('mnist.npz', DATA_URL)

print(path)

data = np.load(path)

# for x in np.nditer(data):
#     print(x)

with np.load(path) as data:
   print(data)
  # train_examples = data['x_train']
  # train_labels = data['y_train']
  # test_examples = data['x_test']
  # test_labels = data['y_test']
