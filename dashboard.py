import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title="Music Data Platform", page_icon="🎵", layout="wide")

# Database connection
engine = create_engine(
    "postgresql+psycopg2://music_user:music_password@localhost:5433/music_db"
)

st.title("🎵 Music Data Platform")
st.caption("Music analytics powered by PostgreSQL + dbt")

# Load data
genre_df = pd.read_sql("SELECT * FROM analytics.genre_performance", engine)

tracks_df = pd.read_sql(
    """
    SELECT
        track_id,
        popularity,
        energy,
        danceability,
        valence,
        tempo
    FROM analytics.fact_track_metrics
    """,
    engine,
)

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Tracks", f"{tracks_df['track_id'].nunique():,}")

with col2:
    st.metric("Total Genres", f"{genre_df['track_genre'].nunique():,}")

with col3:
    st.metric("Avg Popularity", f"{tracks_df['popularity'].mean():.2f}")

st.divider()

# Genre popularity
st.subheader("🔥 Top Genres by Popularity")

top_genres = genre_df.head(10)

fig = px.bar(
    top_genres,
    x="avg_popularity",
    y="track_genre",
    orientation="h",
    labels={"avg_popularity": "Average Popularity", "track_genre": "Genre"},
)

st.plotly_chart(fig, use_container_width=True)

# Audio characteristics
st.subheader("🎧 Audio Characteristics")

fig2 = px.scatter(
    tracks_df.sample(min(5000, len(tracks_df))),
    x="energy",
    y="danceability",
    size="popularity",
    hover_data=["track_id", "popularity"],
    labels={"energy": "Energy", "danceability": "Danceability"},
)

st.plotly_chart(fig2, use_container_width=True)

# Genre table
st.subheader("📊 Genre Performance")

st.dataframe(genre_df, use_container_width=True)
