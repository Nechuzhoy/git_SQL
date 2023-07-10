SELECT title_track, track_duration
  FROM track
 WHERE  track_duration = (SELECT MAX(track_duration) FROM track);

SELECT title_track, track_duration
  FROM track
 WHERE  track_duration >= '00:03:30';

SELECT collection_title, collection_release_year
  FROM collection
 WHERE  collection_release_year <= 2020 AND collection_release_year >= 2018;

SELECT name
  FROM artist
 WHERE name LIKE '% %';

SELECT title_track
  FROM track
 WHERE title_track ILIKE 'мой'
 OR title_track ILIKE '% мой'
 OR title_track ILIKE '% мой %'
 OR title_track ilike 'мой %'
 OR title_track ILIKE 'my'
 OR title_track ILIKE '% my'
 OR title_track ILIKE '% my %'
 OR title_track ilike 'my %';

SELECT genre_id, COUNT(artist_id)
  FROM genre_artist
 GROUP BY genre_id
ORDER BY COUNT(artist_id) desc;

SELECT count(t.track_id)
  FROM track AS t
        JOIN album AS a
        ON t.album_id  = a.album_id
 WHERE a.album_release_year BETWEEN 2019 AND 2020;

SELECT t.album_id, AVG(t.track_duration)
  FROM track AS t
        JOIN album AS a
        ON t.album_id = a.album_id
 GROUP BY t.album_id;

SELECT name
FROM artist AS a3
 WHERE name NOT IN (
 SELECT a."name"
  FROM album_artist AS aa
        JOIN artist AS a
        ON aa.artist_id  = a.artist_id
        JOIN album AS a2
        ON aa.album_id = a2.album_id
 WHERE a2.album_release_year = 2020);

SELECT a2."name"
  FROM collection_track AS ct
        JOIN collection AS c
        ON c.collection_id = ct.collection_id
        JOIN track AS t
        ON t.track_id  = ct.track_id
        JOIN album_artist AS aa
        ON t.album_id = aa.album_id
        JOIN artist AS a2
        ON a2.artist_id = aa.artist_id
 WHERE a2."name" = 'Кино';









