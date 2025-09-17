import pandas as pd
import numpy as np


def clean_rate(series: pd.Series) -> pd.Series:
s = series.astype(str).str.replace('/5', '', regex=False)
s = s.replace('NEW', np.nan).replace('-', np.nan)
return pd.to_numeric(s, errors='coerce')


def clean_cost(series: pd.Series) -> pd.Series:
s = series.astype(str).str.replace(',', '', regex=False)
return pd.to_numeric(s, errors='coerce')
