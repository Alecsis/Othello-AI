import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_othello.envs.board import Board, IllegalMove


class OthelloEnv(gym.Env):
    """
    state: [[0...0], ... [0...0]]
    0 is none
    1 is white
    2 is black
    """
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.board = Board()
        self.current_player_id = 1
    
    def reset(self):
        self.board.reset()
        self.current_player_id = 1

    def step(self, t_action):
        done = False
        reward = 1

        try:
            self.board.do_action(t_action, self.current_player_id)
        except IllegalMove:
            # lose
            done = True
            reward = -1

        # 1 becomes 2 and 2 becomes 1
        self.current_player_id = (self.current_player_id + 1) % 2 + 1

        return self.board.linearize(), reward, done, {"next_player": self.current_player_id}

    def render(self, mode='human', close=False):
        self.board.render()