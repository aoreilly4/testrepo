import pandas as pd 
import os 


df = pd.DataFrame({'TEST':['1','2']})

# Create the Output directory if it doesn't exist
os.makedirs('Output', exist_ok=True)

print(df)

df.to_csv('Output/output.csv', index=False)
