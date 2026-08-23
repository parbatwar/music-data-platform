import pandas as pd

from database import engine

print("Data modeling started")

df = pd.read_sql("SELECT * FROM stg_music_tracks", engine)


# -------------------------
# Dimension: Genres
# -------------------------

genres = (
    df[["track_genre"]]
    .drop_duplicates()
    .sort_values("track_genre")
    .reset_index(drop=True)
)

genres["genre_id"] = genres.index + 1

genres = genres[["genre_id", "track_genre"]]


# -------------------------
# Dimension: Tracks
# -------------------------

tracks = df[
    [
        "track_id",
        "track_name",
        "artists",
        "album_name",
        "duration_ms",
        "explicit",
    ]
].drop_duplicates(subset=["track_id"])


# -------------------------
# Fact: Track Metrics
# -------------------------

metrics = df[
    [
        "track_id",
        "track_genre",
        "popularity",
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
    ]
].copy()


# Add genre_id
metrics = metrics.merge(genres, on="track_genre", how="left")

metrics = metrics.drop(columns=["track_genre"])


# -------------------------
# Load tables
# -------------------------

genres.to_sql("dim_genres", engine, if_exists="replace", index=False)

tracks.to_sql("dim_tracks", engine, if_exists="replace", index=False)

metrics.to_sql("fact_track_metrics", engine, if_exists="replace", index=False)


print(f"Genres: {len(genres)}")
print(f"Tracks: {len(tracks)}")
print(f"Metrics: {len(metrics)}")

print("Data modeling completed")
