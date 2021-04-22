



CREATE DATABASE music_stats;

USE music_stats;

CREATE TABLE song_entry (
	entry_id INT PRIMARY KEY,
    song_name VARCHAR(64),
    artist_name VARCHAR(64),
    album_name VARCHAR(64),
    genre_name VARCHAR(64)
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
    album_name VARCHAR(64),
    genre_name VARCHAR(64),
    FOREIGN KEY (artist_name) REFERENCES artist(artist_name),
    FOREIGN KEY (genre_name) REFERENCES genre(genre_name),
    FOREIGN KEY (album_name) REFERENCES album(album_name)
    );

/* Removes a song from the song table */
DROP procedure if exists delete_entry_proc;
DELIMITER $$
CREATE procedure delete_entry_proc(in song_entry_ varchar(66), in artist_entry_ varchar(66), 
	in album_entry_ varchar(66), in genre_entry_ varchar(66))
BEGIN 
DELETE from song where (song_name = song_entry_ and artist_name = artist_entry_ 
	and album_name = album_entry_ and genre_name = genre_entry_); # limit 1
END $$
DELIMITER ;

/*

DROP procedure if exists add_entry_proc;
DELIMITER $$
CREATE procedure add_entry_proc(in count INT, in song_name_ VARCHAR(64), in artist_name_ VARCHAR(64), 
	in album_name_ VARCHAR(64))
BEGIN 
INSERT INTO song_entry (entry_id, song_name, artist_name, genre_name, album_name)
	values (count+1, song_entry_, artist_entry_, album_entry_, genre_entry_);
END $$
DELIMITER ;
call add_entry_proc()

*/