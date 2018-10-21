#please run using python3

import os
import pandas as pd
import numpy as np

health_per_month = pd.DataFrame()
#initialize pandas dataframes
globe = pd.read_csv("datasets/state_env_data.csv")
health = pd.read_csv("for_udit.csv")

#drop non 2011 data
health = health[health.Year == 2011]
health = health[health.Week % 4 != 0]

def devideFour(x):
    x = int(x/4)
    return x

health['Week'].apply(devideFour)

#train_set, test_set = split_train_set(combined, .2)

print(globe.info())
print(health.head())
