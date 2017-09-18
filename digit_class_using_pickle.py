import pickle

#loading trained model from pickle
estimator = pickle.load(open('digitClass.pickle', 'rb'))

from PIL import Image
from PIL.ImageOps import invert
import numpy as np

def processImage(file):
    img = Image.open(file)
    img2 = img.copy()
    img2 = img2.resize((28, 28))
    img2 = img2.convert('L')
    img2 = invert(img2)
    img2 = np.array(img2)
    img2 = img2.reshape((1, -1))
    return img2
	

#process image	
#always save image as digit.jpg in the same folder as .py files
#you can make it dynamic but for keeping it simple for now
#imgTp = processImage('digit.jpg')

#prediction = estimator.predict(imgTp)
#print (prediction[0])