import pandas as pd
import os
from pathlib import Path

def create_df_by_dictionary(d):
  return pd.DataFrame(d)

def save_csv_file(path, folder, name, df):
  filepath = path + '/' + folder
  os.makedirs(filepath, exist_ok=True)  
  df.to_csv(filepath + '/' + name + '.csv')

def save_csv(name, df):
  dirname = os.path.dirname(os.path.abspath(__file__))
  os.makedirs(dirname, exist_ok=True)
  path = dirname + '/' + name + '.csv'
  if(Path(path).is_file()):
    original_df = pd.read_csv(name + '.csv', index_col=0) #remove the index col
    df = pd.concat([original_df, df], ignore_index=True)
  print(df) 
  df.to_csv(path)
