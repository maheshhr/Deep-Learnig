# -*- coding: utf-8 -*-
"""Deep Learning Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uR_aUXlpB4mlyvqajF-jL9YtKeueKs-A
"""

import pandas as pd

df = pd.read_csv('/content/Iris.csv')

df.head()

df = df.sample(frac = 1) #shuffling the data

df.head()

df.columns

df.drop('Id',axis=1,inplace=True)

df

df['Species'].unique()

dict1 = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}

df['Species'] = df['Species'].map(dict1)

df.head()

import keras

from tensorflow.keras.utils import to_categorical

out_col = to_categorical(df['Species']) #output want to be categorical

input_col = df.drop('Species',axis=1)

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

model = Sequential()

l1 = Dense(16)
l2 = Dense(32)
l3 = Dense(64)
l4 = Dense(128)
l5 = Dense(64)
l6 = Dense(32)
out_layer = Dense(3,activation='softmax')

model.add(l1)
model.add(l2)
model.add(l3)
model.add(l4)
model.add(l5)
model.add(l6)
model.add(out_layer)

import tensorflow as tf

model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics='accuracy')

input_col.head()

out_col[:5]

model.fit(x=input_col, y=out_col, epochs=300)

model.predict([[5.0,2.0,3.5,1.0]])

df

import numpy as np

np.argmax(model.predict([[5.0,2.0,3.5,1.0]]))

dict1