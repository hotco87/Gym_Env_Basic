# Based on https://github.com/openai/gym/blob/b9ef43cb387a93af9728b0fc06cb1723f71bc497/gym/wrappers/README.md

import gym
from gym import envs

#gym에서 제공하는 게임 목록    #print(envs.registry.all())
envids = [spec.id for spec in envs.registry.all()]
for envid in sorted(envids):
    print(envid)

env = gym.make('CartPole-v0') #env = gym.make('MsPacman-v0')

# State Information -> Box(210, 160, 3)
print(env.observation_space) # .shape 사용(tuple로 반환)
print(env.observation_space.high)
print(env.observation_space.low)
print(env.observation_space.shape,"\n") # .shape 사용(tuple로 반환)

# Action Information->  Discrete(2)
print(env.action_space)

# Reward Information-> (-inf, inf)
print(env.reward_range)

# Meta_Data -> {'render.modes': ['human', 'rgb_array'], 'video.frames_per_second': 50}
print(env.metadata)

# Game Name
print(env.spec.id)


###########################################################
## Atari Game - unwrapped ##
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
