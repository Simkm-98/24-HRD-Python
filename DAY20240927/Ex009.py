import keras
import tensorflow as tf
import numpy as np

X = tf.constant([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=tf.float32)
y = tf.constant([0, 1, 1, 0], dtype=tf.float32)

model = keras.models.Sequential(name="XOR")

input = keras.Input(shape=(2,))
model.add(input)
layer1 = keras.layers.Dense(units=4, activation="sigmoid", name='Layer1') # hidden layer
model.add(layer1)
layer2 = keras.layers.Dense(units=2, activation="sigmoid", name='Layer2') # hidden layer
model.add(layer2)
output = keras.layers.Dense(units=1, activation="sigmoid", name='OUTPUT')
model.add(output)

model.summary()

model.compile(loss='mse', optimizer=keras.optimizers.SGD(learning_rate=0.7))
model.fit(X, y, epochs=5_000, verbose=2)
prediction = model.predict(X)
print(np.round(prediction))
model.save('XORGATE.keras')