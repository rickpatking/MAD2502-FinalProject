import pandas as pd
import numpy as np
def load_risk_path_from_csv(csv_file):
    #converts to pandas DataFrame
    df = pd.read_csv(csv_file, header=None)
    #takes in all rows except last two
    sites = df.iloc[:-2].values.astype(float)
    #represents starting points and gets the second to last row
    start = np.array(df.iloc[-2].values, dtype=float)
    #gets the last row representing the endpoint
    stop = np.array(df.iloc[-1].values, dtype=float)

    return sites, start, stop