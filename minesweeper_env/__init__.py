from gym.envs.registration import register

register(
    id='minesweeperenv-v0',
    entry_point='minesweeper_env.envs.minesweeper:MineSweeperEnv'
)
