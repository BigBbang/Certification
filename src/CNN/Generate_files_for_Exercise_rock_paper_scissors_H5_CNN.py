import tensorflow_datasets as tfds

# # See available datasets
# print(tfds.list_builders())
#
# DATASET_NAME = 'rock_paper_scissors'
# # Try this one as well 'horses_or_humans'
#
# (dataset_train_raw, dataset_test_raw), dataset_info = tfds.load(
#     name=DATASET_NAME,
#     data_dir='tmp',
#     with_info=True,
#     as_supervised=True,
#     split=[tfds.Split.TRAIN, tfds.Split.TEST],
# )

# ds = tfds.load('mnist', split='train', as_supervised=True)
# ds = ds.take(1)
#
# for image, label in ds:  # example is (image, label)
#   print(image.shape, label)

# See available datasets
print(tfds.list_builders())

DATASET_NAME = 'horses_or_humans'
# Try this one as well 'horses_or_humans'

(dataset_train_raw, dataset_test_raw), dataset_info = tfds.load(
    name=DATASET_NAME,
    data_dir='tmp',
    with_info=True,
    as_supervised=True,
    split=[tfds.Split.TRAIN, tfds.Split.TEST],
)