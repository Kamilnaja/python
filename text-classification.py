import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses

# url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
# dataset = tf.keras.utils.get_file("aclImdb_v1.tar.gz", url,
#                                   untar=True, cache_dir='.',
#                                   cache_subdir='')
dataset_dir = '.\\aclImdb'

train_dir = os.path.join(dataset_dir, 'train')

remove_dir = os.path.join(train_dir, 'unsup')
if (os.path.exists(remove_dir)):
    shutil.rmtree(remove_dir)
else:
    print("Dir not found")

batch_size = 32
seed = 42

raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'aclImdb/train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed
)
