import os, sys
from typing import Dict

import numpy as np
import pandas as pd

class StateLogger():
    def __init__(self,
                 env_config: Dict,
                 agent_config: Dict,
                 rl_config: Dict,
                 data_save_path: str)-> None:
        self.env_config = env_config
        self.agent_config = agent_config
        self.rl_config = rl_config
        self.data_save_path = data_save_path

        self.env_name = self.env_config['env_name']
        self.agent_name = self.agent_config['agent_name']

        self.episode_data = dict()
        self.step_data = dict()

        self.action_space = None
        self.quantile_num = None

    def initialize_memory(self,
                          max_episode: int,
                          max_step: int,
                          action_space: int=0,
                          quantile_num: int=0)-> None:
        self.action_space = action_space
        self.quantile_num = quantile_num

        self.episode_data['episode_score'] = np.zeros(max_episode, dtype=np.float32)
        self.episode_data['mean_reward']   = np.zeros(max_episode, dtype=np.float32)
        self.episode_data['episode_step']  = np.zeros(max_episode, dtype=np.float32)

        for episode_num in range(max_episode):
            self.step_data[str(episode_num)] = dict()
            self.step_data[str(episode_num)]['num_of_step'] = np.zeros(max_step, dtype=np.float32)

        for act_idx in range(self.action_space):
            if self.agent_name == 'QR_DQN' or self.agent_name == 'QUOTA' or self.agent_name == 'IQN':
                for quant_idx in range(self.quantile_num):
                    self.step_data[str(episode_num)][f'value_{act_idx}_{quant_idx}'] = np.zeros(max_step, dtype=np.float32)
            else:
                self.step_data[str(episode_num)][f'value_{act_idx}'] = np.zeros(max_step, dtype=np.float32)

    def episode_logger(self, episode_num, episode_score, episode_step, env_inner_step):
        self.episode_data['episode_score'][episode_num-1] = episode_score
        self.episode_data['mean_reward'][episode_num-1]   = episode_score/episode_step
        self.episode_data['episode_step'][episode_num-1]  = episode_step

        if self.env_name == 'Platform':
            self.episode_data['env_step'][episode_num-1]  = env_inner_step * 200

        elif self.env_name == 'Goal':
            pass

        else:
            pass

    def step_logger(self, episode_num, episode_step, origin_obs, obs, action_values, action):
        self.step_data[str(episode_num-1)]['num_of_step'][episode_step] = episode_step

        for act_idx in range(self.action_space):
            if self.agent_name == 'QR_DQN' or self.agent_name == 'QUOTA' or self.agent_name == 'IQN':
                for quant_idx in range(self.quantile_num):
                    self.step_data[str(episode_num-1)][f'value_{act_idx}_{quant_idx}'] = action_values[0][act_idx][quant_idx]
            else:
                self.step_data[str(episode_num-1)][f'value_{act_idx}'] = action_values[0][act_idx]
    
    def save_data(self, episode_num):
        if episode_num % 10 == 0:
            episode_data_df = pd.DataFrame(self.episode_data)
            episode_data_df.to_csv(self.data_save_path+'episode_data.csv', mode='w',encoding='UTF-8' ,compression=None)

            episode_step_data_df = pd.DataFrame(self.step_data[str(episode_num-1)])
            if os.path.exists(self.data_save_path + "step_data"):
                if os.name == 'nt':
                    episode_step_data_df.to_csv(self.data_save_path + f"step_data\\episode_{episode_num-1}_data.csv", mode='w',encoding='UTF-8' ,compression=None)
                elif os.name == 'posix':
                    episode_step_data_df.to_csv(self.data_save_path + f"step_data/episode_{episode_num-1}_data.csv", mode='w',encoding='UTF-8' ,compression=None)
            else:
                os.makedirs(self.data_save_path + "step_data")
                if os.name == 'nt':
                    episode_step_data_df.to_csv(self.data_save_path + f"step_data\\episode_{episode_num-1}_data.csv", mode='w',encoding='UTF-8' ,compression=None)
                elif os.name == 'posix':
                    episode_step_data_df.to_csv(self.data_save_path + f"step_data/episode_{episode_num-1}_data.csv", mode='w',encoding='UTF-8' ,compression=None)