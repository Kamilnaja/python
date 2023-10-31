import os 
import pathlib

cwd = os.path.dirname(os.path.abspath(__file__))

data_dir = pathlib.Path(cwd + "/pictures")

image_count = len(list(data_dir.glob('*/*.jpeg')))

## count json files in pictures directory
json_count = len(list(data_dir.glob('*/*.json')))

print(json_count)