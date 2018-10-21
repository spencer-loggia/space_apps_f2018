import pandas as pd
import numpy as np

def split_train_set(data, test_ratio):
    shuf_index = np.randompermutation(len(data))
    test_size = int(len(data) * test(ratio))
    test_indexes = shuf_index[:test_size]
    train_indexes = shuf_index[test_size:]
    return data.iloc[train_indexes], data.iloc[test_indexes]
