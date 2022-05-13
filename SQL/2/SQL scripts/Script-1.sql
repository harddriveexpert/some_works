create or replace procedure insert_data( city_name varchar, city_id int, person_id int, 
last_name varchar, name_person varchar, mid_name varchar, date_per date, sex_per varchar)
language plpgsql
as $$
begin
	begin
		if (exists (select * from city where id_city = city_id) or exists 
		(select * from city where city = city_name)) then 
		raise notice 'Запись с таким city_id уже есть';
	
		else insert into city values (city_id, city_name);
		raise notice 'Занесена запись в таблицу city';
		end if;
	end;
	
	begin
		if exists (select * from person where id_person = person_id) then 
		raise notice 'Запись с таким person_id уже есть';
	
		else insert into person  values (person_id, last_name, 
	name_person, mid_name, date_per, city_id, sex_per);
		raise notice 'Занесена запись в таблицу person';
		end if;
	end;
		
END;
$$;
CALL insert_data('Mosccc', 1234, 312234, 'Shaplavskiy', 'Leonid', 'Pavlovich', '12-29-1999', 'men') ;