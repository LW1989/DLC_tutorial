# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:05:14 2022

@author: Lutz
"""
import deeplabcut

path_config_file = '/home/wallhorn/DLC_Projects/wurm_1-lutz-2023-03-02/config.yaml'
deeplabcut.train_network(path_config_file, displayiters=6000,saveiters=60000, maxiters=600000)
