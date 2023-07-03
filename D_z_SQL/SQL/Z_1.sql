INSERT INTO ganre(title)
VALUES('Rock'), ('Pank'), ('Pop');

INSERT INTO artist(name)
VALUES('Кино'), ('КиШ'), ('Ласковый май'), ('Ария');

INSERT INTO album(album_title, album_release_year)
VALUES('Звезда по имени солнце', 1989 ),
	  ('Камнем по голове', 1996),
	  ('Герой асфальта', 1987),
	  ('Глупые снежинки', 1990);


INSERT INTO track(title_track, track_release_year, album_id, track_duration)
VALUES('Герой фсафльта', 1987, 4, '5:13'),
      ('Улица роз', 1987, 4, '5:56'),
      ('Камнем по голове', 1996, 3, '2:37'),
      ('Дурак и молния', 1996, 3, '1:54'),
      ('Глупые снежинки', 1990, 5, '6:28'),
      ('Я жду тебя, мой', 1990, 5, '5:25'),
      ('Звезда по имени солнце', 1989, 2, '3:46'),
      ('Стук', 1989, 2, '5:31');

INSERT INTO collection(album_title,album_release_year)
VALUES('Концерт в лужниках', 1990),
      ('Акустический альбом', 1996),
      ('30 лет! Юбилейный концерт', 2016),
      ('Лучшее', 2020);

INSERT INTO genre_artist(genre_id, artist_id)
VALUES(1, 1),
      (1, 13),
      (3, 2),
      (4, 3);

INSERT INTO album_artist(album_id,artist_id)
VALUES(2, 1),
      (3, 2),
      (5, 3),
      (4, 13);

INSERT INTO collection_track(collection_id,track_id)
VALUES(2, 12),
      (2, 13),
      (3, 8),
      (3, 9),
      (4, 1),
      (4, 7),
      (5, 10),
      (5, 11);

