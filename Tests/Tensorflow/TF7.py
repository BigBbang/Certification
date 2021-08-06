import tensorflow as tf

# Create Tensor
tensor1 = tf.range(5)
#tf.print(tensor1)
print(tensor1)

# print(dir(tf.data.Dataset))
# Create dataset, this will return object of TensorSliceDataset
dataset = tf.data.Dataset.from_tensor_slices(tensor1)
print(dataset)
print("Original dataset")
for i in dataset:
    print(i)

print('\n')

dataset = dataset.repeat(17).batch(batch_size=3)
print("dataset after applying batch method")
for i in dataset:
    print(i)