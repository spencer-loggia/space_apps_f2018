import os
import random

pop = 1000
name = "person"
f = open("population_data.dat", "a")
f.write("name, group, connectedness, stress, infected? \n")
for i in range(1,pop):
    group = random.randint(1,3)
    sick = random.randint(1,300)
    connectedness = random.randint(1,100)
    stress = random.randint(1,100)
    if sick == 234:
        sick = 1
    else:
        sick = 0
    f.write("name"+ str(i) +","+ str(group) +","+ str(connectedness) +","+ str(stress) +","+ str(sick) + "\n")
