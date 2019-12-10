import random
import numpy as np
from gym import error, spaces, utils


class Agent():
    """
    """
    
    def __init__(self, t_action_space: spaces.Space, t_observation_space: spaces.Space):
        self.action_space = t_action_space
        self.observation_space = t_observation_space
        # self.R = np.zeros(t_action_space.n, t_observation_space.n)

    def get_action(self, t_obsservation):
        return 0