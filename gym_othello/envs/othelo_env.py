import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_othello.envs.board import Board, IllegalMove


class OthelloEnv(gym.Env):
    """
    Colors:
    0 is none
    1 is white
    2 is black
    
    Actions:
    from 0 (first cell) to 63 (last cell) and 64 is "pass"

    Observations:
    from 0 (first cell) to 63 (last cell)
    """
    metadata = {'render.modes': ['human']}
    action_space = spaces.Discrete(65) # 64 cells + 64th is pass
    observation_space = spaces.MultiDiscrete([3] * 64) # 64 cells of 0, 1 or 2

    def __init__(self):
        self.board = Board()
        self.current_player_id = 1
    
    def reset(self):
        self.board.reset()
        self.current_player_id = 1

    def step(self, t_action):
        done = False
        reward = 0

        try:
            self.board.do_action(t_action, self.current_player_id)
            observation = self.board.linearize()
            for cell in observation:
                if cell == self.current_player_id:
                    reward += 1
        except IllegalMove:
            # lose
            done = True
            reward = -1

        # 1 becomes 2 and 2 becomes 1
        if self.current_player_id == 1:
            self.current_player_id = 2
        else:
            self.current_player_id = 1

        return observation, reward, done, {"next_player": self.current_player_id}

    def render(self, mode='human', close=False):
        self.board.render()