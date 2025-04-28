import pandas as pd
import numpy as np
def export_risk_path_to_csv(risk_path):
    all_data = np.vstack([sites, start, stop])
    df = pd.DataFrame(all_data)
    df.to_csv(output_file, header=False, index=False)