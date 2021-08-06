import urllib.request
import pathlib
from pathlib import Path
import os

# File Path/Name to be downloaded from url
DATASET_URL = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip"

# Create destination path directories for file download from url
path_download = Path.cwd() / 'datasets' / 'img' / 'download'

# Create the above destination path in the system
# If parents is true, any missing parents of this path are created as needed
# If exist_ok is true, FileExistsError exceptions will be ignored
Path.mkdir(path_download, parents=True, exist_ok=True)

# Concatenate destination path created before with File Name
file_path = os.path.join(path_download, 'kagglecatsanddogs_3367a.zip')

# Download File from the url
urllib.request.urlretrieve(DATASET_URL, file_path )

print('ciao')