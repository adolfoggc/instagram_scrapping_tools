import pandas as pd
import os

def create_df_by_dictionary(d):
  return pd.DataFrame(d)

def save_csv_file(path, folder, name, df):
  filepath = path + '/' + folder
  os.makedirs(filepath, exist_ok=True)  
  df.to_csv(filepath + '/' + name + '.csv') 


