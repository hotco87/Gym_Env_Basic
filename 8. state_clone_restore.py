## Only Atari Game (ex. pacman)
# https://github.com/openai/gym/blob/master/gym/envs/atari/atari_env.py
# https://github.com/openai/gym/issues/1017
# https://github.com/Jiankai-Sun/RobotArmEnv/blob/master/RobotArmEnv.py

import gym
import numpy as np
import time
import sys


bunch = 20
sequence = 50

#env = gym.make('MsPacmanNoFrameskip-v0')
env = gym.make('MsPacman-ramNoFrameskip-v0')


env.reset()
state_after_reset = env.unwrapped.clone_full_state()

action_sequence = np.random.randint(
    env.action_space.n,
    size=sequence,
)
print(action_sequence)

for i in range(2):
    env.reset() # 게임 상태를 초기화
    env.unwrapped.restore_full_state(state_after_reset)
    while True:
        env.render()  # 게임을 화면에 보여줌

        action = env.action_space.sample() # 랜덤액션

        for sequence_i in range(sequence):
            state, reward, done, info = env.step(action_sequence[sequence_i]) # 주어진 상태에서 랜덤액션 실행
            time.sleep(0.005)

        #print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

        if done:
            print("Finished with reward", reward)
            env.close()
            break