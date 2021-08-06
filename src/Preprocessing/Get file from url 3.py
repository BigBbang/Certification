import tensorflow as tf
import tensorflow.keras.utils as utils

#By default the file at the url origin is downloaded to the cache_dir ~/.keras,
# placed in the cache_subdir datasets, and given the filename fname
path_to_downloaded_file = tf.keras.utils.get_file(
    "flower_photos",
    "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz",
    untar=True)

print(path_to_downloaded_file)