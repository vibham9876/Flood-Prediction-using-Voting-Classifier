from django.db import models
from django.contrib.auth.models import User
import numpy as np
import pickle
import pandas as pd 
from keras.models import load_model

# Load the Keras model from the .h5 file



# Testing phase
svm = pickle.load(open(r"C:\Users\Charlese patel\Music\code\HYBRID MODEL\FRONT END\svm.pkl", 'rb'))
rf = pickle.load(open(r"C:\Users\Charlese patel\Music\code\HYBRID MODEL\FRONT END\RF.pkl", 'rb'))
vot = pickle.load(open(r"C:\Users\Charlese patel\Music\code\HYBRID MODEL\FRONT END\voting.pkl", 'rb'))


def predict(algo,values_list): 
	print(values_list)
	print(algo)
	filter_data =values_list
	data = np.array(filter_data)
	filter_data = data.reshape(1, -1)
	#print(filter_data.shape)
	print(filter_data)
	if algo=='svm':
		y_pred= svm.predict(filter_data)
		return y_pred[0]
	elif algo=='rf':
		y_pred=rf.predict(filter_data)
		return y_pred[0]
	else:
		y_pred=vot.predict(filter_data)
		return y_pred[0]



class UserPredictModel(models.Model):
    image = models.ImageField(upload_to = 'images/')
    label = models.CharField(max_length=20,default='data')

    def __str__(self):
        return str(self.image)
    