import gym
import gym_othello
from  gym_othello.envs.board import Board
import random
from Agent import Agent
import matplotlib.pyplot as plt


def eval_agent(t_player_1: Agent, t_games_number: int):
    # Keep track of scores
    scores1 = []
    scores2 = []

    for i in range(t_games_number):
        score1 = 0
        score2 = 0
        # Reset environment
        observation = env.reset()
        for i in range(30):
            # Player 1
            # action = t_player_1.get_action(observation)
            action = random.choice(env.board.list_actions(1))
            # print(action)
            observation, reward, done, _ = env.step(action)
            score1 = reward
            if done:
                break
            # Player 2
            action = random.choice(env.board.list_actions(2))
            # print(action)
            observation, reward, done, _ = env.step(action)
            score2 = reward
            if done:
                break
        scores1.append(score1)
        scores2.append(score2)

    plt.title("Evolution of scores between Agent1 vs Agent2")
    plt.plot(scores1)
    plt.plot(scores2)
    plt.xlabel("Games played")
    plt.ylabel("Final scores")
    plt.show()


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

def get(i: int, j: int) -> int:
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
    # Open environment
    env = gym.make("othello-v0")

    # Create agents
    agent = Agent(env.action_space, env.observation_space)
    print(agent.R)

    # Close environment
    env.close()