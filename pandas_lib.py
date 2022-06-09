import pandas as pd
from pathlib import Path  

def create_df_by_dictionary(d):
  return pd.DataFrame(d)

def save_csv_file(path, folder, name, df):
  filepath = Path( path + '/' + folder + '/' + name + '.csv')  
  filepath.parent.mkdir(parents=True, exist_ok=True)  
  df.to_csv(filepath) 