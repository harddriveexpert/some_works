CREATE OR REPLACE FUNCTION add_to_log() RETURNS TRIGGER AS $$

    BEGIN
        IF  TG_OP = 'INSERT' or TG_OP = 'UPDATE' THEN
              INSERT INTO logs(tablename,text,added, "user", op_type) values (TG_TABLE_NAME, NEW,NOW(), user, TG_OP);
            RETURN NEW;
        ELSIF TG_OP = 'DELETE' THEN
            INSERT INTO logs(tablename,text,added, "user", op_type) values (TG_TABLE_NAME, OLD,NOW(), user, TG_OP);
            RETURN OLD;
        END IF;
    END;
    $$ LANGUAGE plpgsql;

	CREATE TRIGGER user_person
    AFTER INSERT OR UPDATE OR DELETE ON person FOR EACH ROW EXECUTE PROCEDURE add_to_log ();

    CREATE TRIGGER user_city
    AFTER INSERT OR UPDATE OR DELETE ON city FOR EACH ROW EXECUTE PROCEDURE add_to_log ();

    CREATE TRIGGER user_actors
    AFTER INSERT OR UPDATE OR DELETE ON actors for EACH ROW EXECUTE PROCEDURE add_to_log ();

    CREATE TRIGGER user_directors
    AFTER INSERT OR UPDATE OR DELETE ON directors for EACH ROW EXECUTE PROCEDURE add_to_log ();

    CREATE TRIGGER user_country
    AFTER INSERT OR UPDATE OR DELETE ON country for EACH ROW EXECUTE PROCEDURE add_to_log ();

    CREATE TRIGGER user_film_genres
    AFTER INSERT OR UPDATE OR DELETE ON film_genres for EACH ROW EXECUTE PROCEDURE add_to_log ();

    CREATE TRIGGER user_film_geners_movies
    AFTER INSERT OR UPDATE OR DELETE ON film_geners_movies for EACH ROW EXECUTE PROCEDURE add_to_log ();

    CREATE TRIGGER user_movies
    AFTER INSERT OR UPDATE OR DELETE ON movies for EACH ROW EXECUTE PROCEDURE add_to_log ();
   
    CREATE TRIGGER user_contracts
    AFTER INSERT OR UPDATE OR DELETE ON contracts for EACH ROW EXECUTE PROCEDURE add_to_log ();
   
    CREATE TRIGGER user_film_studios
    AFTER INSERT OR UPDATE OR DELETE ON film_studios for EACH ROW EXECUTE PROCEDURE add_to_log ();
   
    CREATE TRIGGER user_actor_s_role_actors
    AFTER INSERT OR UPDATE OR DELETE ON actor_s_role_actors for EACH ROW EXECUTE PROCEDURE add_to_log ();
   
    CREATE TRIGGER actor_s_role
    AFTER INSERT OR UPDATE OR DELETE ON actor_s_role for EACH ROW EXECUTE PROCEDURE add_to_log ();
   
   


insert into person (id_person, surename, "name", patronymic, date_of_birth, id_city, sex)
values (12332, 'asdf', 'asd', 'qwer', '05-05-1995', 1, 'fmael')


delete from person 
where id_person = 12332

insert into person (id_person, surename, "name", patronymic, date_of_birth, id_city, sex)
values (12332, 'asdf', 'asd', 'qwer', '05-05-1995', 1, 'fmael')


UPDATE  person 
set id_person = 589456
where id_person = 12332