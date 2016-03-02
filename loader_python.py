import numpy as np
import pandas as pd
import commands
from random import randint
import sys

def oracle(x):
    query = "java -cp OracleRegression.jar Oracle " + str(x[1]) + " " + str(x[2]) + " " + str(x[3]) + " " + \
            str(x[4]) + " " + str(x[5]) + " " + " " + str(x[6]) + " " + str(x[7]) + " " + \
            str(x[8]) + " " + str(x[9]) + " " + str(x[10])

    return commands.getoutput(query)


df = pd.read_csv("X_public.csv", sep=",")

y = np.empty(len(df))
y[:] = np.NAN


FILE_NAME = sys.argv[1]
ITER_TO_SAVE = int(sys.argv[2]) 
c = ITER_TO_SAVE
while(True):
    i = randint(0, 999999)
    x = df.iloc[i].as_matrix()
    y[i] = oracle(x)
    
    c -= 1
    if c < 0:
        c = ITER_TO_SAVE
        np.save(FILE_NAME, y)
        print "SAVED"
