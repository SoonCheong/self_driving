#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:37:59 2016
This script is to convert pickle format from Python 3.x to Python 2.x
by changing the pickle protocol to 3
@author: sc15770
"""
import os
import pickle

data_path=os.getcwd()
training_file = data_path+"/train.p"
testing_file = data_path+"/test.p"

with open(training_file, mode='rb') as f:
    train = pickle.load(f)
with open(testing_file, mode='rb') as f:
    test = pickle.load(f)

training2_file = data_path+"/train2.p"
testing2_file = data_path+"/test2.p"    

with open(training2_file, "wb") as f:
    pickle.dump(train, f, protocol=2)
    
with open(testing2_file, "wb") as f:
    pickle.dump(test, f, protocol=2)    
   
