import pandas as pd
def load_data(datapath):
    df = pd.read_csv(datapath)
    print(df.head())
    return df
    