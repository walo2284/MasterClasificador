import tensorflow as tf
import tensorflow_datasets as tfds

datos, metadatos = tfds.load('cats_vs_dogs', as_supervised=True, with_info=True)
