import zipfile
import os

filename = os.path.join(os.getcwd(), "datasets", "glove.6B.100d.txt.zip")

zf = zipfile.ZipFile(filename)
zf.extractall()