# Based on http://gym.openai.com/docs/
# Based on https://github.com/openai/gym/blob/edd0552c1d2f28ff1c46e078bdbfe57ddb5f568e/docs/agents.md
# https://github.com/openai/gym/blob/master/gym/envs/__init__.py
# https://github.com/openai/gym/blob/master/gym/envs/registration.py

import gym
import sys
from gym.envs.registration import register
from gym import wrappers,logger
from colorama import init
import time

init(autoreset=True)  # Reset the terminal mode to display ansi color

register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False}
)

env = gym.make('FrozenLake-v3')

for i in range(3):
    cnt = 0
    reward = 0
    env.reset() # 게임 상태를 초기화
    while True:
        cnt = cnt + 1
        env.render() # 게임을 화면에 보여줌
        # env.render(mode='rgb_array')
        action = env.action_space.sample() # 랜덤액션
        state, reward, done, info = env.step(action) # 주어진 상태에서 랜덤액션 실행
        time.sleep(0.3) # 사람에게 보여질 수 있는 빠르기

        #print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)
        reward += reward

        if done:
            print("Episode Finished with reward", reward)
            print("Episode finished after {} timesteps".format(cnt + 1))
            env.close()
            break

