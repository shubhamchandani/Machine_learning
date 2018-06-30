#!usr/bin/python3
from sklearn.datasets import load_digits
import numpy as np
from sklearn.svm import SVC
dig = load_digits()

training_data  = dig.data
training_target = dig.target
td_original = np.delete(training_data,-1,axis=0)
tt_original = np.delete(training_target,-1)
clf = SVC()
trained = clf.fit(td_original,tt_original)
output = trained.predict(dig.data[-1].reshape(1,64))
print (output)

