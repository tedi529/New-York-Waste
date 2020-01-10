import os
import numpy as np
import pandas as pd

df = pd.read_csv("DSNY_Monthly_Tonnage_Data.csv")

df.iloc[1:].to_csv("Test_csv.csv")