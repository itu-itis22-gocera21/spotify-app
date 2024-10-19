
queries = {
    1: """
        SELECT r.song_name,
               r.artists,
               GROUP_CONCAT(DISTINCT r.country) AS countries,
               MIN(r.snapshot_date) AS start_date,
               MAX(r.snapshot_date) AS end_date,
               MIN(r.popularity) AS min_rank,
               MAX(r.popularity) AS max_rank
        FROM ranks_popularities r
        WHERE r.spotifyid IN (
            SELECT i.spotifyid
            FROM idler_adlar_sozler i
            WHERE i.lyrics LIKE %s
        )
        GROUP BY r.song_name, r.artists
        ORDER BY MAX(r.popularity) DESC;
    """,

    2: """SELECT artists, song_name
            FROM streams
            WHERE streams = (SELECT MAX(streams) FROM streams)
            LIMIT 1;
        """,

    3:"""
SELECT COUNT(DISTINCT song_name) AS song_count,
       GROUP_CONCAT(DISTINCT song_name) AS song_list
FROM (
    SELECT DISTINCT song_name
    FROM idler_adlar_sozler
    WHERE lyrics LIKE '%massaka%'
) AS subquery;

"""
}
