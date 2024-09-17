CREATE TABLE IF NOT EXISTS games(
	game_id int NOT NULL PRIMARY KEY, 
	title varchar(100),
	released_date DATE,
	score NUMERIC(3,2)
);

CREATE TABLE IF NOT EXISTS shops(
	store_id int PRIMARY KEY NOT NULL,
	shop_name varchar(30)
);

CREATE TABLE IF NOT EXISTS units(
	num_unit int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
	game_id int,
	store_id int NOT NULL,
	original_price NUMERIC(4,2),
	discount_price NUMERIC(4,2),
	CONSTRAINT fk_units_games FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT fk_units_shops FOREIGN KEY (store_id) REFERENCES shops(store_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS genres (
	name varchar (100) PRIMARY KEY,
	description varchar (100)
);

CREATE TABLE IF NOT EXISTS games_genres (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	game_id int NOT NULL,
	name_genre varchar (100),
	CONSTRAINT fk_gamesGenres_games FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_gamesGenres_genres FOREIGN KEY (name_genre) REFERENCES genres(name) ON DELETE CASCADE ON UPDATE CASCADE
);