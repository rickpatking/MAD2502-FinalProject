import pandas as pd
import numpy as np
def export_risk_path_to_csv(sites, start, stop, output_file):
    #Stacks parameters vertically in vstack
    all_data = np.vstack([sites, start, stop])
    #converts to a pandas DataFrame from numpy
    df = pd.DataFrame(all_data)
    #writes DataFrame as a CSV file
    df.to_csv(output_file, header=False, index=False)