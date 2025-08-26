import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

# Load and preprocess the MNIST dataset
def load_mnist():
    (x_train, _), (_, _) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.astype('float32') / 255.0
    x_train = x_train.reshape(-1, 28 * 28)
    return x_train

# Generator model
def build_generator():
    model = tf.keras.Sequential([
        layers.Dense(128, activation='relu', input_shape=(100,)),
        layers.Dense(784, activation='sigmoid')
    ])
    return model

# Discriminator model
def build_discriminator():
    model = tf.keras.Sequential([
        layers.Dense(128, activation='relu', input_shape=(784,)),
        layers.Dense(1, activation='sigmoid')
    ])
    return model

# GAN training loop
def train_gan(generator, discriminator, x_train, epochs=10000, batch_size=64):
    cross_entropy = tf.keras.losses.BinaryCrossentropy()
    d_optimizer = tf.keras.optimizers.Adam(1e-4)
    g_optimizer = tf.keras.optimizers.Adam(1e-4)

    for epoch in range(epochs):
        # Train discriminator
        idx = np.random.randint(0, x_train.shape[0], batch_size)
        real_imgs = x_train[idx]
        noise = np.random.normal(0, 1, (batch_size, 100))
        fake_imgs = generator.predict(noise, verbose=0)

        with tf.GradientTape() as tape:
            real_output = discriminator(real_imgs, training=True)
            fake_output = discriminator(fake_imgs, training=True)
            d_loss = cross_entropy(tf.ones_like(real_output), real_output) + \
                    cross_entropy(tf.zeros_like(fake_output), fake_output)
        grads = tape.gradient(d_loss, discriminator.trainable_variables)
        d_optimizer.apply_gradients(zip(grads, discriminator.trainable_variables))

        # Train generator
        noise = np.random.normal(0, 1, (batch_size, 100))
        with tf.GradientTape() as tape:
            generated_imgs = generator(noise, training=True)
            fake_output = discriminator(generated_imgs, training=True)
            g_loss = cross_entropy(tf.ones_like(fake_output), fake_output)
        grads = tape.gradient(g_loss, generator.trainable_variables)
        g_optimizer.apply_gradients(zip(grads, generator.trainable_variables))

        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, D Loss: {d_loss.numpy():.4f}, G Loss: {g_loss.numpy():.4f}")
            show_generated_image(generator)

def show_generated_image(generator):
    noise = np.random.normal(0, 1, (1, 100))
    generated_img = generator.predict(noise, verbose=0)[0].reshape(28, 28)
    plt.imshow(generated_img, cmap='gray')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    x_train = load_mnist()
    generator = build_generator()
    discriminator = build_discriminator()
    train_gan(generator, discriminator, x_train, epochs=5000, batch_size=64)
