from minesweeper_env.envs.stage import Stage

import gym
import numpy as np

class MineSweeperEnv(gym.Env):
    def __init__(self, width=9, height=9, bomb_count=10):
        super().__init__()

        self.width = width
        self.height = height
        self.bomb_count = bomb_count

        self.action_space = gym.spaces.MultiDiscrete([self.width, self.height])
        self.observation_space = gym.spaces.MultiDiscrete([8 for _ in range(2*self.width*self.height)])
        self.reward_range = [-10., 100.]

        self.stage = Stage(width, height, bomb_count)

        self.reset()

    def get_observation(self):
        observation = []
        for y in range(self.height):
            for x in range(self.width):
                is_covered = self.stage.get_cell(x, y).is_covered
                observation.append(int(is_covered))
                if is_covered:
                    observation.append(0)
                else:
                    cell_value = self.stage.get_surrounded_count(x, y)
                    observation.append(cell_value)
        return np.array(observation, dtype=np.int32)

    def reset(self):
        observation = self.get_observation()

        return observation


    def step(self, point2d):
        x, y = point2d

        cell = self.stage.get_cell(x, y)
        cell.step()
        self.stage.decrement_cell()

        observation = self.get_observation()
        reward = -10 * int(cell.has_bomb or not cell.is_covered)
        done = cell.has_bomb or (self.stage.remain_cells == self.bomb_count)
        if done: reward = 100
        info = {}

        return observation, reward, done, info

    def render(self):
        horizontal_line = "-" * (self.width * 2 + 1)

        print(horizontal_line)
        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                cell = self.stage.get_cell(x, y)
                if cell.is_covered: line += " "
                else: line += str(self.stage.get_surrounded_count(x, y))
                line += "|"
            print(line)
            print(horizontal_line)