



CREATE DATABASE music_stats;

USE music_stats;

CREATE TABLE song_entry (
	entry_id INT PRIMARY KEY,
    song_name VARCHAR(64),
    artist_name VARCHAR(64),
    genre_name VARCHAR(64),
    album_name VARCHAR(64)
    );
    
CREATE TABLE genre (
	genre_name VARCHAR(64) PRIMARY KEY
    );
    
CREATE TABLE artist (
	artist_name VARCHAR(64) PRIMARY KEY
    );

CREATE TABLE album (
    album_name VARCHAR(64) PRIMARY KEY,
    artist_name VARCHAR(64),
    FOREIGN KEY (artist_name) REFERENCES artist(artist_name)
    );
    
CREATE TABLE song (
	song_id INT PRIMARY KEY,
    song_name VARCHAR(64),
    artist_name VARCHAR(64),
    genre_name VARCHAR(64),
    album_name VARCHAR(64),
    FOREIGN KEY (artist_name) REFERENCES artist(artist_name),
    FOREIGN KEY (genre_name) REFERENCES genre(genre_name),
    FOREIGN KEY (album_name) REFERENCES album(album_name)
    );


    
    
    