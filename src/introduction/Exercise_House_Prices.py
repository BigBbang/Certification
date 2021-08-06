import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras
from keras import models
from keras import layers

def house_price(bedrooms):
    return 0.5 * (bedrooms + 1)

# model = keras.models.Sequential(
#     [
#         keras.layers.Dense(units=1, input_shape=[1])
#     ]
# )

model = models.Sequential()
model.add(layers.Dense(1, input_shape=(1,)))

model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.01),
              loss=keras.losses.mean_squared_error)

xs = np.array([1, 2, 3, 4, 5, 6], dtype=int)
ys = house_price(xs)

plt.scatter(xs,ys)
plt.show()

model.fit(x=xs, y=ys, epochs=1000, verbose=1)

print(f'House value is {model.predict([7])} hundreds of $')