SELECT
    t.track_id,
    g.track_genre,
    s.popularity,
    s.duration_ms,
    s.danceability,
    s.energy,
    s.loudness,
    s.speechiness,
    s.acousticness,
    s.instrumentalness,
    s.liveness,
    s.valence,
    s.tempo
FROM {{ ref('stg_music_tracks') }} s
JOIN {{ ref('dim_tracks') }} t
    ON s.track_id = t.track_id
JOIN {{ ref('dim_genres') }} g
    ON s.track_genre = g.track_genre