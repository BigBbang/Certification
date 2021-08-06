# https://docs.python.org/3/library/pathlib.html

import pathlib
from pathlib import Path

# Create new train and validation directories
path_train = Path.cwd() / 'datasets' / 'images' / 'cats_and_dogs' / 'train'
path_validation = Path.cwd() / 'datasets' / 'images' / 'cats_and_dogs' / 'validation'
# If parents is true, any missing parents of this path are created as needed
# If exist_ok is true, FileExistsError exceptions will be ignored
Path.mkdir(path_train, parents=True, exist_ok=True)
Path.mkdir(path_validation, parents=True, exist_ok=True)



