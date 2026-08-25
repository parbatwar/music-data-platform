import os

import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

st.set_page_config(
    page_title="Music Data Platform",
    page_icon="🎵",
    layout="wide",
)

# Database connection
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

required_vars = {
    "DB_HOST": DB_HOST,
    "DB_PORT": DB_PORT,
    "DB_NAME": DB_NAME,
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD,
}

missing = [name for name, value in required_vars.items() if not value]

if missing:
    st.error(f"Missing database environment variables: {', '.join(missing)}")
    st.stop()

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}" f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

st.title("🎵 Music Data Platform")
st.caption("Music analytics powered by PostgreSQL + dbt")

# Load data
genre_df = pd.read_sql(
    "SELECT * FROM analytics.genre_performance",
    engine,
)

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
    st.metric(
        "Total Tracks",
        f"{tracks_df['track_id'].nunique():,}",
    )

with col2:
    st.metric(
        "Total Genres",
        f"{genre_df['track_genre'].nunique():,}",
    )

with col3:
    st.metric(
        "Avg Popularity",
        f"{tracks_df['popularity'].mean():.2f}",
    )

st.divider()

# Genre popularity
st.subheader("🔥 Top Genres by Popularity")

top_genres = genre_df.head(10)

fig = px.bar(
    top_genres,
    x="avg_popularity",
    y="track_genre",
    orientation="h",
    labels={
        "avg_popularity": "Average Popularity",
        "track_genre": "Genre",
    },
)

st.plotly_chart(fig, use_container_width=True)

# Audio characteristics
st.subheader("🎧 Audio Characteristics")

sample_df = tracks_df.sample(min(5000, len(tracks_df)))

fig2 = px.scatter(
    sample_df,
    x="energy",
    y="danceability",
    size="popularity",
    hover_data=["track_id", "popularity"],
    labels={
        "energy": "Energy",
        "danceability": "Danceability",
    },
)

st.plotly_chart(fig2, use_container_width=True)

# Genre table
st.subheader("📊 Genre Performance")

st.dataframe(
    genre_df,
    use_container_width=True,
)
