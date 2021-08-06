import tensorflow as tf
import tensorflow.keras.utils as utils


#     cache_dir='.' means store the file under the current work directory.
# folder 'datasets' is created by default if not existing
tf.keras.utils.get_file(
    "flower_photos",
    "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz",
    untar=True,
    cache_dir='.')