import pandas as pd

dataset = pd.read_csv('data/raw/time_series_60min_singleindex.csv')
germany_data = dataset['DE_load_actual_entsoe_transparency']
germany_data = germany_data.iloc[1:]

germany_data.columns = [
    "timestamp",
    "load_mw"
]

germany_data.to_csv('data/processed/germany_load.csv')
