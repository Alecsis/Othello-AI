import random
import numpy as np
from gym import error, spaces, utils
import tensorflow as tf

class Agent():
    """
    """

    def __init__(self, t_action_space: spaces.Space, t_observation_space: spaces.Space):
        self.action_space = t_action_space
        self.observation_space = t_observation_space
        # self.R = np.zeros(t_action_space.n, t_observation_space.n)
        self.model = self.make_model(
            t_observation_space.shape, t_action_space.shape)

    def make_model(self, t_input_shape, t_output_shape):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Conv2D(64, kernel_size=(5, 5), strides=(1, 1),
                  activation='relu', input_shape=(8,8,1)))
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(tf.keras.layers.Conv2D(128, (5, 5), activation='relu'))
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(1000, activation = 'relu'))
        model.add(tf.keras.layers.Dense(t_output_shape[0]))
        model.compile(  loss=tf.keras.losses.categorical_crossentropy,
                        optimizer=keras.optimizers.SGD(learning_rate=0.01),
                        metrics=['accuracy'])
        
        return model

    def get_action(self, t_observation):
        return 0