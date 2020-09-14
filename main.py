from stable_baselines.common.policies import MlpPolicy
from stable_baselines import PPO2

import os
import gym
import minesweeper_env

log_dir = "./logs"
model_dir = "./models"
os.makedirs(log_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)

# 環境準備と学習
env = gym.make("minesweeperenv-v0")

model = PPO2(MlpPolicy, env, verbose=1, tensorboard_log="./logs")
model.learn(total_timesteps=10000000)
model.save("./models/minesweeper_learned_10000000")