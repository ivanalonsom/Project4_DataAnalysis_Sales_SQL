CREATE TABLE IF NOT EXISTS games(
	gameID int NOT NULL PRIMARY KEY, 
	title varchar(100),
	release_date DATE,
	scores NUMERIC(3,2)
);

CREATE TABLE IF NOT EXISTS shops(
	store_id int PRIMARY KEY NOT NULL,
	store_name varchar(30)
);

CREATE TABLE IF NOT EXISTS units(
	num_unit int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
	gameID int,
	store_id int NOT NULL,
	original_price NUMERIC(5,2),
	discount_price NUMERIC(5,2),
	CONSTRAINT fk_units_games FOREIGN KEY (gameID) REFERENCES games(gameID) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT fk_units_shops FOREIGN KEY (store_id) REFERENCES shops(store_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS genres (
	genre_name varchar (100) PRIMARY KEY,
	description varchar (100)
);

CREATE TABLE IF NOT EXISTS games_genres (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	gameID int NOT NULL,
	genre_name varchar (100),
	CONSTRAINT fk_gamesGenres_games FOREIGN KEY (gameID) REFERENCES games(gameID) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_gamesGenres_genres FOREIGN KEY (genre_name) REFERENCES genres(genre_name) ON DELETE CASCADE ON UPDATE CASCADE
);