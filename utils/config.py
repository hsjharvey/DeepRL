# -*- coding:utf-8 -*-
import tensorflow as tf


class Config:
    device = tf.device('/gpu:0')

    def __init__(self):
        # categorical DQN parameters
        self.Categorical_Vmin = -10
        self.Categorical_Vmax = 10
        self.Categorical_n_atoms = 51

        # environment
        self.input_dim = (1, 4)
        self.action_dim = 2

        self.episodes = 1000
        self.steps = 1000


        # agent
        self.batch_size = 32
        self.replay_buffer_size = 100  # must > batch size
        self.discount_rate = 0.9
        self.learning_rate = 0.1
