import pandas as pd
import numpy as np
import pickle
from sklearn import neighbors
from sqlalchemy import create_engine

def getState(latitude, longitude):
    """
    Returns the state given a latitude and longitude.
    Written for SpaceApps Challenge 2018.

    We didn't want to pay $8 per 1000 queries to Google's API.
    """
    cities_df = pd.read_pickle('city_df.pickle')
    states_df = pd.read_pickle('state_df.pickle')

    kdtree = pickle.load(open('KDTree.pickle','rb'))

    dist, ind = kdtree.query([[latitude, longitude]])

    state_id = cities_df.iloc[ind[0][0]][0]
    state = states_df.iloc[state_id - 1,2]

    return state


if __name__ == "__main__":
    # read in data from excel sheets
    cities_df = pd.read_excel('us_cities.xlsx')
    states_df = pd.read_excel('us_states.xlsx')

    # clean up the parentheses
    cities_df.iloc[:,4] = [float(x[:-1]) for x in cities_df.iloc[:,4]]
    states_df.iloc[:,0] = [int(x[1:]) for x in states_df.iloc[:,0]]
    states_df.iloc[:,2] = [x[:-1] for x in states_df.iloc[:,2]]

    city_pts = cities_df.as_matrix(columns=cities_df.columns[3:])

    # build 2-d kd-tree, only built once in this file and pickled so we can reuse the tree
    tree = neighbors.KDTree(city_pts, leaf_size=2)

    pickle.dump(tree, open('KDTree.pickle','wb'))

    cities_df.to_pickle("city_df.pickle")
    states_df.to_pickle("state_df.pickle")

    print(getState(42.92, -123.299))
