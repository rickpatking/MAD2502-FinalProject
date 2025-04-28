import pandas as pd
import numpy as np
def load_risk_path_from_csv(csv_file):
    df = pd.read_csv(csv_file, header=None)
    sites = df.iloc[:-2].values.astype(float)
    start = np.array(df.iloc[-2].values, dtype=float)
    stop = np.array(df.iloc[-1].values, dtype=float)

    return sites, start, stop