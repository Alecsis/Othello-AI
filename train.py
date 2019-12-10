import gym
import gym_othello
from  gym_othello.envs.board import Board
import random


def test_board():
    board = Board()
    player_id = 1
    cnt = 0
    while not board.is_done():
        cnt += 1
        possible_actions = board.list_actions(player_id)
        action = random.choice(possible_actions)
        board.do_action(action, player_id)
        board.render()
        if player_id == 1:
            player_id = 2
        else:
            player_id = 1
    print(cnt)

def get(i, j):
    return i * 8 + j

def qlearning():
    # S: current state
    # A: current action
    # S': state after A
    # a: learning rate
    a = 0.9
    # y: discount factor
    y = 0.95
    # maxaQ(S',A): highest Q value for any move in the next state S'
    #   ie. the Q value of the best move
    # Q(S,A) = Q(S,A) + a*(y*maxaQ(S',a) - Q(S,A))
    # Q(S,A) = (1-a)*Q(S,A)+a*y*maxaQ(S',a)
    pass

if __name__ == "__main__":
    print("[.] Beginning simulation...")
    env = gym.make("othello-v0")
    observation = env.reset()
    env.render()

    action = get(3, 5)
    observation, reward, done, info = env.step(action)
    env.render()

    action = get(2, 5)
    observation, reward, done, info = env.step(action)
    env.render()

    # action = env.action_space.sample() # get(2, 5)
    # observation, reward, done, info = env.step(action)
    # env.render()

    print("Reward: {}".format(reward))
    print("Done: {}".format(done))

    env.close()
