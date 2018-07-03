import gym
from gym.envs.registration import register
from colorama import init
import time

init(autoreset=True)  # Reset the terminal mode to display ansi color

register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False}
)

# gym 환경(env)에 대해 정의를 할 때에는 gym.make('spec.id')를 사용한다.
# 환경을 수정하고 싶으면 register 정의

env = gym.make('FrozenLake-v3')

for i in range(3):
    reward = 0
    env.reset() # 게임 상태를 초기화
    start_time = time.time()
    cnt = 0
    while True:
        cnt = cnt+1
        env.render(mode='human') # 게임을 화면에 보여줌, env.render(mode='rgb_array')
        action = env.action_space.sample() # 랜덤액션
        state, reward, done, info = env.step(action) # 주어진 상태에서 랜덤액션 실행
        time.sleep(0.05) # 사람에게 보여질 수 있는 빠르기
        #print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)
        reward += reward

        if done:
            e = int(time.time() - start_time)
            print('{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))
            print('{0:.2f} seconds'.format(e%(60)))
            print('{0} step'.format(cnt))
            env.close()
            break