import gym

env = gym.make('LunarLander-v2')
env.reset()
for eps in range(5):
    observation = env.reset() # starts new episode AND returns initial observation
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample() # take a random action
        observation, reward, done, info = env.step(action)
        if done:
            print(f"{eps+1}th episode finished after {t+1} timesteps")
            break
env.close()