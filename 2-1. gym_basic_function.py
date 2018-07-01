# Based on https://github.com/openai/gym/blob/b9ef43cb387a93af9728b0fc06cb1723f71bc497/gym/wrappers/README.md

import gym
from gym import envs

#print(envs.registry.all())
envids = [spec.id for spec in envs.registry.all()]
for envid in sorted(envids):
    print(envid)
env = gym.make('CartPole-v0')
#env = gym.make('MsPacman-v0')

# Box(210, 160, 3), Box(4,)
print(env.observation_space) # .shape 사용(tuple로 반환)
print(env.observation_space.high)
print(env.observation_space.low)
print(env.observation_space.shape,"\n") # .shape 사용(tuple로 반환)

# Discrete(9), Discrete(2)
print(env.action_space)

# (-inf, inf)
print(env.reward_range)

# {'render.modes': ['human', 'rgb_array'], 'video.frames_per_second': 50}
print(env.metadata)

# MsPacman-v0, 'CartPole-v0'
print(env.spec.id)
