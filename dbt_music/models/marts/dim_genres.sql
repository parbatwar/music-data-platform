SELECT DISTINCT
    track_genre
FROM {{ ref('stg_music_tracks') }}
WHERE track_genre IS NOT NULL