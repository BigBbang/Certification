# https://keras.io/api/preprocessing/image/

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image

import pathlib
from pathlib import Path

IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
IMAGE_SIZE = (IMAGE_WIDTH, IMAGE_HEIGHT)
IMAGE_CHANNELS = 3

# Get training and validation images from directory
image_datagenerator = image.ImageDataGenerator(rescale=1 / 255.)

# If your directory structure is:
# main_directory/
# ...class_a/
# ......a_image_1.jpg
# ......a_image_2.jpg
# ...class_b/
# ......b_image_1.jpg
# ......b_image_2.jpg
# Then calling image_dataset_from_directory(main_directory, labels='inferred')
# will return a tf.data.Dataset that yields batches of images from the subdirectories
# class_a and class_b, together with labels 0 and 1 (0 corresponding to class_a
# and 1 corresponding to class_b).

training_generator = image_datagenerator.flow_from_directory(
    directory=Path.cwd() / 'datasets' / 'images' / 'cats_and_dogs' / 'train',
    target_size=IMAGE_SIZE,
    class_mode='binary',
    batch_size=20
)

validation_generator = image_datagenerator.flow_from_directory(
    directory=Path.cwd() / 'datasets' / 'images' / 'cats_and_dogs' / 'validation',
    target_size=IMAGE_SIZE,
    class_mode='binary',
    batch_size=20 )


print('Ciao')