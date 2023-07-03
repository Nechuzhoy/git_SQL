SELECT title_track, track_duration
  FROM track
 WHERE  track_duration = (SELECT MAX(track_duration) FROM track)

SELECT title_track, track_duration
  FROM track
 WHERE  track_duration >= '3:30'

SELECT album_title, album_release_year
  FROM collection
 WHERE  album_release_year <= 2020 AND album_release_year >= 2018

SELECT name
  FROM artist
 WHERE name LIKE '% %'

SELECT title_track
  FROM track
 WHERE title_track LIKE '%мой%'

SELECT genre_id, COUNT(artist_id)
  FROM genre_artist
 GROUP BY genre_id
ORDER BY COUNT(artist_id) DESC

SELECT c.collection_id , c.track_id, g.album_release_year
  FROM collection_track AS c
        JOIN collection AS g
        ON g.collection_id  = c.collection_id
 WHERE g.album_release_year BETWEEN 2019 AND 2020

SELECT t.album_id, AVG(t.track_duration)
  FROM track AS t
        JOIN album AS a
        ON t.album_id = a.album_id
 GROUP BY t.album_id

SELECT a."name" , a2.album_release_year
  FROM album_artist AS aa
        JOIN artist AS a
        ON aa.artist_id  = a.artist_id
        JOIN album AS a2
        ON aa.album_id = a2.album_id
 WHERE a2.album_release_year < 2020

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
 WHERE a2.'name' = 'Кино'








