WITH ranked_tracks AS (
    SELECT
        source_row_id,
        track_id,
        artists,
        album_name,
        track_name,
        popularity,
        duration_ms,
        explicit,
        danceability,
        energy,
        key,
        loudness,
        mode,
        speechiness,
        acousticness,
        instrumentalness,
        liveness,
        valence,
        tempo,
        time_signature,
        track_genre,

        ROW_NUMBER() OVER (
            PARTITION BY track_id
            ORDER BY source_row_id
        ) AS row_num

    FROM public.raw_music_tracks

    WHERE track_id IS NOT NULL
      AND artists IS NOT NULL
      AND album_name IS NOT NULL
      AND track_name IS NOT NULL
)

SELECT
    source_row_id,
    track_id,
    artists,
    album_name,
    track_name,
    popularity,
    duration_ms,
    explicit,
    danceability,
    energy,
    key,
    loudness,
    mode,
    speechiness,
    acousticness,
    instrumentalness,
    liveness,
    valence,
    tempo,
    time_signature,
    track_genre

FROM ranked_tracks
WHERE row_num = 1