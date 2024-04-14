import tensorflow as tf

from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.layers.experimental.preprocessing import RandomFlip, RandomRotation

BATCH_SIZE = 32
IMG_SIZE = (160, 160)


def augment_data():
  data_augmentation = tf.keras.Sequential()
  data_augmentation.add(RandomFlip('horizontal'))
  data_augmentation.add(RandomRotation(0.2))

  return data_augmentation

preprocess_input = tf.keras.applications.vgg16.preprocess_input
def sculpture_model(image_shape = IMG_SIZE, data_augmentation = augment_data()):

  input_shape = image_shape + (3,)
  base_model = tf.keras.applications.VGG16(input_shape=input_shape, include_top = False,
                                          weights = 'imagenet')

  base_model.trainable = False

  inputs = tf.keras.Input(shape = input_shape)
  x = data_augmentation(inputs)
  x = preprocess_input(x)
  x = base_model(x, training = False)

  x = tf.keras.layers.GlobalAveragePooling2D()(x)
  x = tf.keras.layers.Dropout(rate = 0.1)(x)

  outputs = tf.keras.layers.Dense(5, activation = 'softmax')(x)

  model = tf.keras.Model(inputs, outputs)

  return model
