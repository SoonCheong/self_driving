import os
import numpy as np
import tensorflow as tf
import pickle 
import cv2
import h5py
import json
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten
from keras.layers import Convolution2D, MaxPooling2D, BatchNormalization
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

data_path=os.getcwd()+"/data"
training_file = data_path+"/train.p"

with open(training_file, mode='rb') as f:
    train = pickle.load(f)
   
X_train, Y_train = train['ctr_frames'], train['steerings']


# TODO: Compile and train the model.
model=Sequential()

# Convolutional 1
model.add(Convolution2D(nb_filter=24,nb_row=5, nb_col=5, subsample=(2,2),
                       border_mode='valid', activation='relu', input_shape=(60,160,3)))
model.add(Convolution2D(nb_filter=36,nb_row=5, nb_col=5, subsample=(2,2),
                       border_mode='valid' ,activation='relu'))
model.add(Convolution2D(nb_filter=48,nb_row=5, nb_col=5, subsample=(2,2),
                       border_mode='valid' ,activation='relu'))
					   
model.add(Convolution2D(nb_filter=64,nb_row=3, nb_col=3, subsample=(1,1),
                       border_mode='valid' ,activation='relu'))
#model.add(Convolution2D(nb_filter=64,nb_row=3, nb_col=3, subsample=(1,1),
#                       border_mode='valid' ,activation='relu'))					   

# Dense 
model.add(Flatten())
model.add(Dense(1164, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(10, activation='relu'))

# Output
model.add(Dense(1))

adam=Adam(lr=5e-3, decay=0.5)

model.compile(loss='mean_squared_error', 
              optimizer='adam', 
              metrics=['accuracy'])

history=model.fit(X_train, Y_train, nb_epoch=1, batch_size=200, verbose=1)


# **Validation Accuracy**: (fill in here)

# In[109]:

#score = model.evaluate(X_test, Y_test, verbose=1, batch_size=500)

# Save model and weights 
model_json=model.to_json()
with open("model.json","w") as json_file:
    json.dump(model_json, json_file)

model.save_weights('model.h5')


