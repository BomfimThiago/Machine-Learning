import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pickle

# first training is_slippery is False, after we set it to True
def run(episodes, is_training=True, render=False):
    env = gym.make('FrozenLake-v1', map_name="8x8", is_slippery=True, render_mode="human" if render else None)

    if is_training:
        Q = np.zeros((env.observation_space.n, env.action_space.n)) # q_table init a 64 x 4 array with zeros
    else:
        with open("frozen_lake8x8.pkl", "rb") as f:
            Q = pickle.load(f)
    
    alpha = 0.9 # alpha or learning rate
    gamma = 0.9 # gamma or discount factor

    # episolon greed algorithm
    epsilon = 1 # 1 = 100% random actions
    epsilon_decay_rate = 0.0001
    rng = np.random.default_rng()

    rewards_per_episode = np.zeros(episodes)
    total_rewards = []

    for i in range(episodes):
        state = env.reset()[0]
        terminated = False
        truncated = False
        total_reward = 0

        while (not terminated and not truncated):
            if is_training and rng.random() < epsilon:
                action = env.action_space.sample() # actions: 0=left, 1=down, 2=right, 3=up
            else:
                action = np.argmax(Q[state,:])

            new_state, reward, terminated, truncated, _ = env.step(action)
            total_reward += reward

            if is_training:
                # 𝑄(𝑠,𝑎)= 𝑄(𝑠,𝑎) + 𝛼( 𝑟 + 𝛾max(𝑎′𝑄𝑠′,𝑎′) − 𝑄(𝑠,𝑎)) Bellman Equation
                Q[state,action] = Q[state,action] + alpha * (
                    reward + gamma * np.max(Q[new_state,:]) - Q[state,action]
                )
            
            state = new_state


        epsilon = max(epsilon - epsilon_decay_rate, 0)

        if(epsilon == 0):
            alpha = 0.0001

        total_rewards.append(total_reward)
        if reward == 1:
            rewards_per_episode[i] = 1

    env.close()

    sum_rewards = np.zeros(episodes)
    for t in range(episodes):
        sum_rewards[t] = np.sum(rewards_per_episode[max(0, t-100):(t+1)])

    plt.figure(figsize=(10, 5))
    plt.plot(np.convolve(total_rewards, np.ones(100)/100, mode='valid'))
    plt.title('Rewards Moving Average (100-episode window)')
    plt.xlabel('Episode')
    plt.ylabel('Average Reward')
    plt.grid(True)
    plt.savefig('frozen_lake8x8.png')

    if is_training:
        f = open("frozen_lake8x8.pkl", "wb")
        pickle.dump(Q, f)
        f.close()

if __name__ == "__main__":
    # episodes is the number of times we gonna train our model
    run(15000)
    # run(1000, is_training=False, render=True)