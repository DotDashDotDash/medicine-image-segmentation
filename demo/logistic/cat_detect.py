# This demo is for cat recofonition

import sys
sys.path.append('./lr_utils.py')
import numpy as np
import matplotlib.pyplot as plt
import h5py
from lr_utils import load_dataset

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

index = 25
plt.show(train_set_x_orig[index])
print("train_set_y=" + str(train_set_y))