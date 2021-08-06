import tensorflow as tf
import os

_URL = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"

# By default the file at the url origin is downloaded to the cache_dir ~/.keras, placed in the
# cache_subdir datasets, and given the filename fname. The final location of a file example.txt
# would therefore be ~/.keras/datasets/example.txt.
zip_file = tf.keras.utils.get_file(origin=_URL,
                                   fname="flower_photos.tgz",
                                   extract=True)

print(zip_file)
# C:\Users\I043594\.keras\datasets\flower_photos.tgz

print(os.path.dirname(zip_file))
# C:\Users\I043594\.keras\datasets

base_dir = os.path.join(os.path.dirname(zip_file), 'flower_photos')
print(base_dir)
# C:\Users\I043594\.keras\datasets\flower_photos
