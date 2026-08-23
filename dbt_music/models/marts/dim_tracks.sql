SELECT
    track_id,
    artists,
    album_name,
    track_name,
    track_genre
FROM {{ ref('stg_music_tracks') }}