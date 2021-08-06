import os
import csv
import pathlib
from pathlib import Path
import numpy as np

# IMAGE_SIZE = 28
labels = []
images = []

file_name = Path.cwd() / 'datasets' / 'csv' / 'sign_mnist_test.csv'

with open(file_name, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)

    for row in reader:
        labels.append(row[0])
# Take into account current row starting from position [1]
        images.append(np.array_split(row[1:], 28))



print(images)

print('ciao')