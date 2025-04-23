import pandas as pd
import numpy as np
def export_risk_path_to_csv(risk_path):
    df = pd.DataFrame(risk_path)
    df.to_csv(output_file, header=False)