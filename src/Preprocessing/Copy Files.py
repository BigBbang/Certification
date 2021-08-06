from pathlib import Path

source = Path('C:/Users/I043594/PycharmProjects/Certification/src/CNN/datasets/images/cats_and_dogs/train/dogs')
target = Path('C:/Users/I043594/PycharmProjects/Certification/src/Preprocessing/datasets/images/cats_and_dogs/train\dogs')

counter = 0

for obj in source.iterdir():
    if obj.is_file():
        obj.rename(target / obj.name)
        counter += 1
    if counter > 2:
        break