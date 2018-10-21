#please run using python3

import os
import pandas as pd
import numpy as np

health_per_month = pd.DataFrame()
#initialize pandas dataframes
globe = pd.read_csv("datasets/state_env_data.csv")
health = pd.read_csv("for_udit.csv")

for index, row in health.iterrows():
    month = int((row[2]/4))
    if(month == 0):
        month = 1
    health.set_value(index, 'Week', month)
health.rename(columns={'Week': 'month'}, inplace=True)

#train_set, test_set = split_train_set(combined, .2)

health.to_csv("health_data.csv")
