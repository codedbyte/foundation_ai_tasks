import tensorflow as tf
import matplotlib.pyplot as plt
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") /255.0

print("Training data shape", x_train.shape)
print("Training data labels:", y_train.shape)

print("Test data shape: ", x_test.shape)
print("Test data label: ", y_test.shape)

plt.imshow(x_train[0], cmap="grey")
plt.show()