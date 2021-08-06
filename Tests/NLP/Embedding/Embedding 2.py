# Understanding Embedding Layer in Keras
# https://medium.com/analytics-vidhya/understanding-embedding-layer-in-keras-bbe3ff1327ce

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding
import numpy as np

model = Sequential()
embedding_layer = Embedding(input_dim=10,output_dim=4,input_length=2)
model.add(embedding_layer)
model.compile('adam','mse')

print(embedding_layer.weights)

# input_data = np.array([[1,2]])
# pred = model.predict(input_data)
# print(input_data.shape)
# print(pred)

print(model.summary())

