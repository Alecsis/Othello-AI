import gym
import gym_othello
from  gym_othello.envs.board import Board
import random

if __name__ == "__main__":
    print("[.] Beginning simulation...")
    # env = gym.make("othello-v0")
    # observation = env.reset()
    # env.render()

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

    # action = 3*8 + 5
    # observation, reward, done, info = env.step(action)
    # env.render()

    # action = 2*8 + 3
    # observation, reward, done, info = env.step(action)
    # env.render()

    # action = 1*8 + 2
    # observation, reward, done, info = env.step(action)
    # env.render()

    # action = 1*8 + 3
    # observation, reward, done, info = env.step(action)
    # env.render()

    # action = -1
    # observation, reward, done, info = env.step(action)
    # env.render()

    # print("Reward: {}".format(reward))
    # print("Done: {}".format(done))

    # env.close()
