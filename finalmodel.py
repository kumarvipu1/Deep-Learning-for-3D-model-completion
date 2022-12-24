import tensorflow as tf
from tensorflow.keras.layers import (Conv1D, Dense, Flatten, Reshape)
from tensorflow.keras.models import Model

class EncoderDecoder(Model):
    def __init__(self):
        super(EncoderDecoder, self).__init__()
        self.encoder = tf.keras.Sequential([
            Conv1D(128, kernel_size=1),
            Conv1D(256, kernel_size=1),
            Conv1D(512, kernel_size=1),
            #Conv1D(1000, kernel_size=1),
            Flatten(),
            Dense(1000)
        ])
        self.decoder = tf.keras.Sequential([
            Dense(1000, activation=None),
            Dense(1000, activation=None),
            Dense(2000*3, activation=None),
            Reshape((2000, 3))
        ])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded