# Based on http://gym.openai.com/docs/
# Based on https://github.com/openai/gym/blob/edd0552c1d2f28ff1c46e078bdbfe57ddb5f568e/docs/agents.md
# https://github.com/openai/gym/blob/master/gym/envs/__init__.py
# https://github.com/openai/gym/blob/master/gym/envs/registration.py

# GYM Installation
# pip install gym
# gym 환경을 한 번 돌려보자!

import gym
import time

env = gym.make('MsPacmanNoFrameskip-v0')

for i in range(1):
    reward = 0
    env.reset() # 게임 상태를 초기화
    start_time = env._episode_started_at
    while True:
        env.render(mode='human') # 게임을 화면에 보여줌, env.render(mode='rgb_array')
        action = env.action_space.sample() # 랜덤액션
        state, reward, done, info = env.step(action) # 주어진 상태에서 랜덤액션 실행
        time.sleep(0.005) # 사람에게 보여질 수 있는 빠르기
        #print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)
        reward += reward

        if done:
            e = int(time.time() - start_time)
            print('{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))
            print('{0:.2f} seconds'.format(env._elapsed_seconds))
            print('{0} step'.format(env._elapsed_steps))
            env.close()
            break

