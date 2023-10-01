import numpy as np
import tensorflow as tf
new_model = tf.keras.models.load_model('my_model.keras')

batch_size = 128
img_height = 612
img_width = 370

class_names = ['analog', 'digital']

gshock_url = "https://img01.ztat.net/article/spp-media-p1/21d3261ab23a3319aa6bf608eae3bcfe/a67f2ae3fcb44351a14bb2514678dfab.jpg?imwidth=1800"
sunflower_path = tf.keras.utils.get_file('Gshock', origin=gshock_url)

img = tf.keras.utils.load_img(
    sunflower_path, target_size=(img_height, img_width)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create a batch

predictions = new_model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)
