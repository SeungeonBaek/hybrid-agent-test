
# Q-PAMDP  
Q_PAMDP_Vanilla_agent_config = {'agent_name': 'Q-PAMDP', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'batch_size': 128, 'warm_up': 1024, 
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
Q_PAMDP_Vanilla_agent_config['extension'] = {'name': 'Vanilla', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}


# PA-DDPG
PA_DDPG_Vanilla_agent_config = {'agent_name': 'PA-DDPG', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'batch_size': 128, 'warm_up': 1024, 
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
PA_DDPG_Vanilla_agent_config['extension'] = {'name': 'Vanilla', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}


# P-DQN  
P_DQN_Vanilla_agent_config = {'agent_name': 'P-DQN', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'batch_size': 128, 'warm_up': 1024, 
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
P_DQN_Vanilla_agent_config['extension'] = {'name': 'Vanilla', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}


# MP-DQN  
MP_DQN_Vanilla_agent_config = {'agent_name': 'MP-DQN', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'batch_size': 128, 'warm_up': 1024, 
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
MP_DQN_Vanilla_agent_config['extension'] = {'name': 'Vanilla', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}


# HPPO  
HPPO_Vanilla_agent_config = {'agent_name': 'HPPO', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'batch_size': 128, 'warm_up': 1024, 
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
HPPO_Vanilla_agent_config['extension'] = {'name': 'Vanilla', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}
