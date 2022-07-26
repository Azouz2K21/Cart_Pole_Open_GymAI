import gym
import random

env = gym.make("CartPole-v1")


def Renadom_games():
    for episode in range(1000):
        env.reset()

        for t in range(500):
            env.render

            action = env.action_space.sample()

            next_state, reward, done, info = env.step(action)

            print(t, next_state, reward, done, info)
            if done:
                break


Renadom_games()
