'''
Created on 06.07.2018

@author: xsun
'''
import gym
if __name__ == '__main__':
    env = gym.make('CartPole-v0')
    env.reset()
    for _ in range(100):
        env.render()
        env.step(env.action_space.sample()) # take a random action