# Based on https://github.com/openai/gym/blob/b9ef43cb387a93af9728b0fc06cb1723f71bc497/gym/wrappers/README.md
## Only Atari Game (ex. pacman)

import gym
import numpy as np
import time
import sys

env = gym.make('MsPacman-v0')

print("\n")
print(env.observation_space) # hight, width, 3
print(env.action_space)
print(env.reward_range)

# Atari_only
# unwrapped 을 이용하여 내부환경(Atari 고유 환경)에 접근할 수 있음.
# https://github.com/openai/gym/blob/master/gym/envs/atari/atari_env.py
print(env.unwrapped.get_keys_to_action()) # dictionary, .keys(), .values()
print(env.unwrapped.get_action_meanings())
# state = env.unwrapped.clone_full_state()
# print(state)
# print(np.shape(state))
# print(env.seed())
# print(env.unwrapped._get_image())
# get_ram = env.unwrapped._get_ram()
# print(np.shape(get_ram))