import os
import pandas as pd
import math

#time step in days
dt = 1
data = pd.read_csv("./population_data.csv")

#population density of campus per square mile
popden = 7000

nonull = data.copy()
nonull = nonull.dropna()

total_pop = data.shape[0]
numberinfected = nonull.shape[0]
numberSucceptable = total_pop - numberinfected
numberrecovered = 0;

epsilon = .05 #arbitrary deimmunization constant
recoverate = .1 #arbitrary recovery rate

for i in range(0,60):
    #define relation of beta to density
    beta = .4 * math.log(popden)

    #current mental state of campus
    avg_stress = data['stress'].mean()

    #relate beta to population stress
    beta = beta * (avg_stress/100)

    avgcon = nonull['connectedness'].mean()

    #modify beta based on infected connectedness
    beta = beta * (avgcon / 100)


    #preform calculation
    deltasucceptable = ((-1 * beta)*numberSucceptable * numberinfected / data.shape[0]) + epsilon * numberrecovered
    deltainfected = (beta*numberSucceptable * numberinfected / data.shape[0]) - recoverate * numberinfected
    deltarecovered = (recoverate * numberinfected) - epsilon * numberrecovered

    numberSucceptable += deltasucceptable
    numberinfected += deltainfected
    numberrecovered += deltarecovered

    print("suc: " + str(numberSucceptable) + "  inf: " + str(numberinfected) + "  rec: " + str(numberrecovered)  + "\n")
