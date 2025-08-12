import pandas as pd 
import os 


df = pd.DataFrame({'TEST':['1','2']})

df.to_csv('Output/output.csv', index=False)
