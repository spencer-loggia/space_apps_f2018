#!/usr/bin/env python
# coding: utf-8

# In[5]:


#get proper modules
import pandas as pd
import numpy as np
import sklearn as sk

#load data (all feature should be combined to one dframe here)
data = pd.read_csv("datasets/amalgamated_data.csv")
health = pd.read_csv("datasets/health_data.csv")

for index, row in data.iterrows():
    state = (row['state'])
    state = state[1:len(state)-1]
    data.set_value(index, 'state', state)

#show head to ensure proper import
data.head()


# In[7]:


#data.to_csv("datasets/amalgamated_data.csv")

#merge data and health
data = data.merge(health, left_on=['state','month','year'], right_on=['State','month','Year'])


# In[8]:


data.head()


# In[12]:


data.drop(data.columns[[0,1,2,11,13]], 1, inplace=True)
data.info()


# In[32]:


from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

def split_train_set(data, test_ratio):
    shuf_index = np.random.permutation(len(data))
    test_size = int(len(data) * test_ratio)
    test_indexes = shuf_index[:test_size]
    train_indexes = shuf_index[test_size:]
    return data.iloc[train_indexes], data.iloc[test_indexes]

#handle dataframe and numpy array transformations
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def _init_(self, attribute_names):
        self.atrribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values

#drop nulls (failsafe)
data.dropna()

#spilt training and test set (USE TRAIN FOR ALL REGRESSORS)
train_data, test_data = split_train_set(data, .2)

#seperate labels and attributes
train_data_labels = train_data['Infected']
train_data.drop(data.columns[[9]], 1, inplace=True)
train_data.drop(['state', 'State'], 1, inplace = True)

train_data.info()

#add additional transformation tasks to the below sklearn pipeline
#standardize data (use devide by variance standardization to minimize outlier impact)
stpipeline = Pipeline([
    ('std_scaler', StandardScaler()),
])
train_data_prepped = stpipeline.fit_transform(train_data)


# In[47]:


from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

def display_scores(scores):
    print("Score: ")
    print(scores)
    print("\nMean: ")
    print(scores.mean())
    print("\nStd. Dev.: ")
    print(scores.std())



# In[49]:


forest_reg = RandomForestRegressor()
forest_reg.fit(train_data_prepped, train_data_labels)

forest_scores = cross_val_score(forest_reg, train_data_prepped, train_data_labels,
    scoring = "neg_mean_squared_error", cv=10)
forest_rmse_scores = np.sqrt(-scores)

display_scores(forest_rmse_scores)


# In[ ]:
train_data_prepped = stpipeline.fit_transform(train_data)


# In[ ]:


lin_prediction = lin_reg.predict(test_data_prepared)
mse = mean_squared_error(test_data_labels, lin_prediction)
rmse = np.sqrt(mse)

print(rmse)
