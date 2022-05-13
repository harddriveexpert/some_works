user="postgres"
password=""
host="localhost"
port="5432"
database="postgres"

create = """CREATE TABLE Actor_s_role
(
	ID_roles             INTEGER NOT NULL ,
	name_of_role         VARCHAR(20) NOT NULL 
);


ALTER TABLE Actor_s_role
	ADD CONSTRAINT  XPKActor_s_role PRIMARY KEY (ID_roles);

CREATE TABLE Actors
(
	ID_actor             INTEGER NOT NULL 
);



ALTER TABLE Actors
	ADD CONSTRAINT  XPKActors PRIMARY KEY (ID_actor);

CREATE TABLE Actor_s_role_Actors
(
	ID_roles             INTEGER NOT NULL ,
	ID_actor             INTEGER NOT NULL 
);


ALTER TABLE Actor_s_role_Actors
	ADD CONSTRAINT  XPKActor_s_role_Actors PRIMARY KEY (ID_roles,ID_actor);

CREATE TABLE City
(
	ID_city              INTEGER NOT NULL ,
	City                 VARCHAR(30) NOT NULL 
);


ALTER TABLE City
	ADD CONSTRAINT  XPKCity PRIMARY KEY (ID_city);

CREATE TABLE Country
(
	ID_country           INTEGER NOT NULL ,
	Country              VARCHAR(30) NOT NULL 
);


ALTER TABLE Country
	ADD CONSTRAINT  XPKCountry PRIMARY KEY (ID_country);

CREATE TABLE Film_studios
(
	ID_studio            INTEGER NOT NULL ,
	name_of_studio       VARCHAR(100) NOT NULL ,
	ID_city              INTEGER NOT NULL 
);



ALTER TABLE Film_studios
	ADD CONSTRAINT  XPKFilm_studios PRIMARY KEY (ID_studio);

CREATE TABLE Movies
(
	ID_movi              INTEGER NOT NULL ,
	Name_of_movi         VARCHAR(30) NOT NULL ,
	date_movi            INTEGER NOT NULL ,
	ID_country           INTEGER NOT NULL ,
	ID_director          INTEGER NOT NULL ,
	budget               INTEGER NOT NULL CHECK (budget > 0)
);


ALTER TABLE Movies
	ADD CONSTRAINT  XPKMovies PRIMARY KEY (ID_movi);

CREATE TABLE Contracts
(
	ID_contract          INTEGER NOT NULL ,
	ID_studio            INTEGER NOT NULL ,
	ID_movi              INTEGER NOT NULL ,
	date_contract        DATE NOT NULL ,
	ID_actor             INTEGER NOT NULL ,
	Number_of_contract   INTEGER NOT NULL UNIQUE CHECK (Number_of_contract > 0)
);



ALTER TABLE Contracts
	ADD CONSTRAINT  XPKContracts PRIMARY KEY (ID_contract);

CREATE TABLE Directors
(
	ID_director          INTEGER NOT NULL 
);



ALTER TABLE Directors
	ADD CONSTRAINT  XPKDirectors PRIMARY KEY (ID_director);

CREATE TABLE Film_genres
(
	ID_ganre             INTEGER NOT NULL ,
	ganre_name           VARCHAR(30) NOT NULL 
);



ALTER TABLE Film_genres
	ADD CONSTRAINT  XPKFilm_genres PRIMARY KEY (ID_ganre);

CREATE TABLE Film_geners_Movies
(
	ID_ganre             INTEGER NOT NULL ,
	ID_movi              INTEGER NOT NULL 
);



ALTER TABLE Film_geners_Movies
	ADD CONSTRAINT  XPKFilm_geners_Movies PRIMARY KEY (ID_ganre,ID_movi);

CREATE TABLE Person
(
	ID_person            INTEGER NOT NULL ,
	Surename             VARCHAR(30) NOT NULL ,
	Name                 VARCHAR(30) NOT NULL ,
	Patronymic           VARCHAR(30) NULL ,
	Date_of_Birth        DATE NOT NULL ,
	ID_city              INTEGER NOT NULL ,
	Sex                  text NOT NULL 
);

CREATE TABLE logs
(
    "tablename" text,
    "text" text,
    "added" timestamp without time zone,
    "user" text,
    "op_type" text
);



ALTER TABLE Person
	ADD CONSTRAINT  XPKPerson PRIMARY KEY (ID_person);


ALTER TABLE Actors
	ADD CONSTRAINT R_13 FOREIGN KEY (ID_actor) REFERENCES Person (ID_person) ON DELETE CASCADE;

ALTER TABLE Actor_s_role_Actors
	ADD CONSTRAINT R_2 FOREIGN KEY (ID_roles) REFERENCES Actor_s_role (ID_roles);

ALTER TABLE Actor_s_role_Actors
	ADD CONSTRAINT R_3 FOREIGN KEY (ID_actor) REFERENCES Actors (ID_actor);

ALTER TABLE Film_studios
	ADD CONSTRAINT R_16 FOREIGN KEY (ID_city) REFERENCES City (ID_city);

ALTER TABLE Movies
	ADD CONSTRAINT R_8 FOREIGN KEY (ID_director) REFERENCES Directors (ID_director);

ALTER TABLE Movies
	ADD CONSTRAINT R_9 FOREIGN KEY (ID_country) REFERENCES Country (ID_country);

ALTER TABLE Contracts
	ADD CONSTRAINT R_4 FOREIGN KEY (ID_studio) REFERENCES Film_studios (ID_studio);

ALTER TABLE Contracts
	ADD CONSTRAINT R_5 FOREIGN KEY (ID_actor) REFERENCES Actors (ID_actor);

ALTER TABLE Contracts
	ADD CONSTRAINT R_7 FOREIGN KEY (ID_movi) REFERENCES Movies (ID_movi);

ALTER TABLE Directors
	ADD CONSTRAINT R_14 FOREIGN KEY (ID_director) REFERENCES Person (ID_person) ON DELETE CASCADE;

ALTER TABLE Film_geners_Movies
	ADD CONSTRAINT R_11 FOREIGN KEY (ID_ganre) REFERENCES Film_genres (ID_ganre);

ALTER TABLE Film_geners_Movies
	ADD CONSTRAINT R_12 FOREIGN KEY (ID_movi) REFERENCES Movies (ID_movi);

ALTER TABLE Person
	ADD CONSTRAINT R_17 FOREIGN KEY (ID_city) REFERENCES City (ID_city);"""

drop = """
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

"""

imp = """
COPY city FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/city_table.txt' DELIMITER'|';
COPY person FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/person_table.txt' DELIMITER '|' ;
COPY country FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/country_table.txt' DELIMITER '|' ;
COPY film_genres FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/film_gan_table.txt' DELIMITER '|' ;
COPY film_studios FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/studio_table.txt' DELIMITER '|' ;
COPY actors FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/actor.txt' DELIMITER '|' ;
COPY directors FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/directors_table.txt' DELIMITER '|' ;
COPY actor_s_role FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/rol.txt' DELIMITER '|' ;
COPY actor_s_role_actors FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/actor_s_role_actors_table.txt' DELIMITER '|' ;
COPY movies FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/movi_table.txt' DELIMITER '|' ;
COPY contracts FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/contract_table.txt' DELIMITER '|' ;
COPY film_geners_movies FROM '/Users/leoto/Desktop/work/DB_LAB_2/csv/film_geners_movies_table.txt' DELIMITER '|' ;"""


export = """
COPY city TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/city_table.txt' DELIMITER',' ;
COPY person TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/person_table.txt' DELIMITER ',' ;
COPY country TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/country_table.txt' DELIMITER ',' ;
COPY film_genres TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/film_gan_table.txt' DELIMITER ',' ;
COPY film_studios TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/studio_table.txt' DELIMITER ',' ;
COPY actors TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/actor.txt' DELIMITER ',' ;
COPY directors TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/directors_table.txt' DELIMITER ',' ;
COPY actor_s_role TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/rol.txt' DELIMITER ',' ;
COPY actor_s_role_actors TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/actor_s_role_actors_table.txt' DELIMITER ',' ;
COPY movies TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/movi_table.txt' DELIMITER ',' ;
COPY contracts TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/contract_table.txt' DELIMITER ',' ;
COPY film_geners_movies TO '/Users/leoto/Desktop/work/DB_LAB_2/csv1/film_geners_movies_tablev.txt' DELIMITER ',' ;"""


