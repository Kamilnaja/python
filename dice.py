import tensorflow as tf
from tensorflow_probability import distributions as tfd


def roll_dice (num_rols): 
  distributions = tfd.Uniform(low=1, high=7) 
  samples= distributions.sample(num_rols)

  return tf.constant(samples, dtype=tf.int32)

roll_dice(10)
print(roll_dice(10))

help = help(tf.ones);
print(help)