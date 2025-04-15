import pandas as pd
import numpy as np
def load_risk_path_from_csv(csv_file):
    df = pd.read_csv(csv_file, header=None)
    risk_path = df.values.astype(float)
    return risk_path

