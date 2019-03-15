#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:16:25 2019

@author: kbg
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from math import sqrt

from Gonzales import Gonzales

print(chr(27) + "[2J")


DATA_PATH = "data"
print()
print(os.listdir(DATA_PATH))
print()
player_attr_raw = pd.read_csv(os.path.join(DATA_PATH, 'Player_Attributes.csv'))
print()
print("Raw Data Shape:", player_attr_raw.shape)
print()
player_attr = player_attr_raw.dropna()
print()
print("Cleaned Data Shape:", player_attr.shape)
print()
unique_foot = player_attr['preferred_foot'].unique()

unqiue_off_rate = player_attr['attacking_work_rate'].unique()

unqiue_def_rate = player_attr['defensive_work_rate'].unique()

print()
print()
player_attr.info()
print()
print()
vectorized_players_df = player_attr.drop(columns=['id','player_fifa_api_id',
                                               'player_api_id', 'date', 
                                               'preferred_foot', 'attacking_work_rate',
                                               'defensive_work_rate', 'overall_rating',
                                            'potential'])
print()
print()
print()
print('Vector Shape:', vectorized_players_df.shape)
print()
print()
print()
vectorized_players_df.info()

description = vectorized_players_df.describe()

vectorized_players = vectorized_players_df.values

clusters, three_cen_cost, three_mean_cost, centers = Gonzales(vectorized_players, vectorized_players[0,:], k=2)

print(clusters.shape)

print(centers)