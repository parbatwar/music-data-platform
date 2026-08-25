WITH genre_stats AS (
    SELECT
        track_genre,
        COUNT(*) AS track_count,
        ROUND(AVG(popularity)::numeric, 2) AS avg_popularity,
        ROUND(AVG(energy)::numeric, 2) AS avg_energy,
        ROUND(AVG(danceability)::numeric, 2) AS avg_danceability
    FROM {{ ref('fact_track_metrics') }}
    GROUP BY track_genre
)

SELECT
    *,
    RANK() OVER (
        ORDER BY avg_popularity DESC
    ) AS popularity_rank
FROM genre_stats
ORDER BY popularity_rank