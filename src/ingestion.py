import pandas as pd
from database import engine

df = pd.read_csv("data/raw/dataset.csv")

df = df.rename(columns={"Unnamed: 0": "source_row_id"})

df.to_sql(name="raw_music_tracks", con=engine, if_exists="append", index=False)

print("Data loaded into PostgreSQL")
