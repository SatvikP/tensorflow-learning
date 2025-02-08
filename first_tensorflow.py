import tensorflow as tf
import numpy as np

# Print TensorFlow version
print(f"TensorFlow version: {tf.__version__}")

# Create some simple tensors
x = tf.constant([1, 2, 3], dtype=tf.float32)
y = tf.constant([4, 5, 6], dtype=tf.float32)

# Perform basic operations
addition = x + y
multiplication = x * y

print("\nTensor x:", x.numpy())
print("Tensor y:", y.numpy())
print("\nAddition result:", addition.numpy())
print("Multiplication result:", multiplication.numpy())

# Create a simple neural network layer
layer = tf.keras.layers.Dense(units=1, input_shape=[1])
print("\nNeural network layer created successfully!")