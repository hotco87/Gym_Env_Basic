import gym
import time

env = gym.make('MsPacmanNoFrameskip-v0')

for i in range(1):
    reward = 0
    env.reset() # 게임 상태를 초기화
    start_time = env._episode_started_at
    while True:
        env.render() # 게임을 화면에 보여줌
        action = env.action_space.sample() # 랜덤액션
        state, reward, done, info = env.step(action) # 주어진 상태에서 랜덤액션 실행

        reward += reward

        if done:
            print("Episode Finished with reward", reward)
            e = int(time.time() - start_time)
            print('{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))
            print('{0:.2f} seconds'.format(env._elapsed_seconds))
            print('{0} step'.format(env._elapsed_steps))
            env.close()
            break

