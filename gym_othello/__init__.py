from gym.envs.registration import register

register(
    id='othello-v0',
    entry_point='gym_othello.envs:OthelloEnv',
)