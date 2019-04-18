import tensorflow as tf 

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

training_images = training_images.reshape(60000, 28, 28, 1)
training_images = training_images / 255.0
test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activator='relu'),
    tf.keras.layers.Dense(10, activator='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
