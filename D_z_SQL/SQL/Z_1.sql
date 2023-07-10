INSERT INTO genre(title)
VALUES('Rock'), ('Pank'), ('Pop');

INSERT INTO artist(name)
VALUES('Кино'), ('КиШ'), ('Ария'), ('Ласковый май');

INSERT INTO album(album_title, album_release_year)
VALUES('Звезда по имени солнце', 1989 ),
	  ('Камнем по голове', 1996),
	  ('Герой асфальта', 1987),
	  ('Глупые снежинки', 2020);


INSERT INTO track(title_track, track_release_year, album_id, track_duration)
values ('Звезда по имени солнце', 1989, 1, '00:03:46'),
       ('Стук', 1989, 1, '00:05:31'),
	   ('Камнем по голове', 1996, 2, '00:02:37'),
       ('Дурак и молния', 1996, 2, '00:01:54'),
       ('Герой фсафльта', 1987, 3, '00:05:13'),
       ('Улица роз', 1987, 3, '00:05:56'),
       ('Глупые снежинки', 1990, 4, '00:06:28'),
       ('Я жду тебя, мой', 1990, 4, '00:05:25');

INSERT INTO collection(collection_title,collection_release_year)
VALUES('Концерт в лужниках', 1990),
      ('Акустический альбом', 1996),
      ('30 лет! Юбилейный концерт', 2016),
      ('Лучшее', 2020);

INSERT INTO genre_artist(genre_id, artist_id)
VALUES(1, 1),
      (1, 3),
      (2, 2),
      (3, 4);

INSERT INTO album_artist(album_id, artist_id)
VALUES(1, 1),
      (2, 2),
      (3, 3),
      (4, 4);

INSERT INTO collection_track(collection_id,track_id)
VALUES(1, 1),
      (1, 2),
      (2, 3),
      (2, 4),
      (3, 5),
      (3, 6),
      (4, 7),
      (4, 8);
