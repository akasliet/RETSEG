import tensorflow as tf
from tensorflow.keras import layers

model = tf.keras.Sequential([
  layers.Conv2D(64, 3, activation='relu', padding='same', input_shape=(256, 256, 3)),
  layers.BatchNormalization(),
  layers.Conv2D(64, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.MaxPooling2D(),
  layers.Conv2D(128, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(128, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.MaxPooling2D(),
  layers.Conv2D(256, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(256, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(256, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.MaxPooling2D(),
  layers.Conv2D(512, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(512, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(512, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.MaxPooling2D(),
  layers.Conv2D(512, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(512, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(512, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.UpSampling2D(),
  layers.Conv2D(256, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(256, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(256, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.UpSampling2D(),
  layers.Conv2D(128, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(128, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.UpSampling2D(),
  layers.Conv2D(64, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(64, 3, activation='relu', padding='same'),
  layers.BatchNormalization(),
  layers.Conv2D(2, 1, activation='softmax', padding='same')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, validation_data=(x_val, y_val))
