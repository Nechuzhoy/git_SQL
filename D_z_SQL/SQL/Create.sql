CREATE TABLE IF NOT EXISTS genre
(
    genre_id SERIAL PRIMARY KEY,
    title VARCHAR(30) NOT NULL
    UNIQUE(title)
);

CREATE TABLE IF NOT EXISTS artist
(
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(60) NOT NULL
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS genre_artist
(
    genre_artist_id SERIAL PRIMARY KEY,
    genre_id  INT REFERENCES genre(genre_id) NOT NULL,
    artist_id INT REFERENCES artist(artist_id) NOT NULL
);

CREATE TABLE IF NOT EXISTS album
(
    album_id SERIAL PRIMARY KEY,
    album_title VARCHAR(30) NOT NULL,
    album_release_year INTEGER NOT NULL
    UNIQUE(album_title)
);

CREATE TABLE IF NOT EXISTS album_artist
(
    album_artist_id SERIAL PRIMARY KEY,
    album_id  INT REFERENCES album(album_id) NOT NULL,
    artist_id INT REFERENCES artist(artist_id) NOT NULL
);

CREATE TABLE IF NOT EXISTS track
(
    track_id SERIAL PRIMARY KEY,
    title_track VARCHAR(60) NOT NULL,
    track_release_year INTEGER NOT NULL,
    track_duration TIME not null,
    album_id  INT REFERENCES album(album_id)
);

CREATE TABLE IF NOT EXISTS collection
(
    collection_id SERIAL PRIMARY KEY,
    album_title VARCHAR(30) NOT NULL,
    album_release_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS collection_track
(
    collection_track_id SERIAL PRIMARY KEY,
    title_track VARCHAR(60) NOT NULL,
    collection_id  INT REFERENCES collection(collection_id),
    track_id INT REFERENCES track(track_id)
);
