import tensorflow as tf
import keras
import numpy as np

loaded_model = keras.models.load_model('XORGATE.keras')

loaded_model.summary()

X_test = tf.constant([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=tf.float32)

predictions = loaded_model.predict(X_test)
print(np.round(predictions))