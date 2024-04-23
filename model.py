import tensorflow as tf

from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.layers import RandomFlip, RandomRotation
from tensorflow.keras.regularizers import l1
BATCH_SIZE = 32
IMG_SIZE = (256, 256)


def augment_data():


  data_augmentation = tf.keras.Sequential([
      tf.keras.layers.RandomFlip('horizontal'),
      tf.keras.layers.Lambda(lambda img: tf.image.random_contrast(img, lower=0.5, upper=1.5)),
      tf.keras.layers.Lambda(lambda img:  tf.image.random_brightness(img, max_delta=2.0))
  ])
  return data_augmentation

preprocess_input = tf.keras.applications.efficientnet.preprocess_input

def sculpture_model(image_shape = IMG_SIZE, data_augmentation = augment_data()):

  input_shape = image_shape + (3,)
  base_model = tf.keras.applications.EfficientNetB3(input_shape=input_shape, include_top = False,
                                          weights = 'imagenet')

  base_model.trainable = False

  inputs = tf.keras.Input(shape = input_shape)
  x = data_augmentation(inputs)
  x = preprocess_input(x)
  x = base_model(x, training = False)

  x = tf.keras.layers.GlobalAveragePooling2D()(x)
  x = tf.keras.layers.Dropout(rate = 0.5)(x)

  weight_initializer1 = tf.keras.initializers.HeNormal(seed=13)
  weight_initializer2 = tf.keras.initializers.HeNormal(seed=23)
  weight_initializer3 = tf.keras.initializers.HeNormal(seed=33)

  #x = tf.keras.layers.Dense(256,kernel_initializer = weight_initializer1,activation='relu')(x)
  x = tf.keras.layers.Dense(128,kernel_initializer = weight_initializer2, activation='relu')(x)
  x = tf.keras.layers.Dropout(rate = 0.2)(x)
  x = tf.keras.layers.Dense(64,kernel_initializer = weight_initializer3, activation='relu')(x)
  x = tf.keras.layers.Dropout(rate = 0.2)(x)

  outputs = tf.keras.layers.Dense(12, activation = 'softmax')(x)

  model = tf.keras.Model(inputs, outputs)

  return model