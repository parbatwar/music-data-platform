import pandas as pd

from database import engine

print("Transformation started")

df = pd.read_sql("SELECT * FROM raw_music_tracks", engine)

print(f"Raw rows: {len(df)}")

# Remove exact duplicate records
df = df.drop_duplicates(
    subset=[
        "track_id",
        "artists",
        "album_name",
        "track_name",
        "popularity",
        "duration_ms",
        "explicit",
        "danceability",
        "energy",
        "key",
        "loudness",
        "mode",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "time_signature",
        "track_genre",
    ]
)

# Remove unnecessary source column
df = df.drop(columns=["source_row_id"])

# Handle missing text values
df["artists"] = df["artists"].fillna("Unknown")
df["album_name"] = df["album_name"].fillna("Unknown")
df["track_name"] = df["track_name"].fillna("Unknown")

print(f"Clean rows: {len(df)}")

df.to_sql("stg_music_tracks", engine, if_exists="replace", index=False)

print("Staging table created")
