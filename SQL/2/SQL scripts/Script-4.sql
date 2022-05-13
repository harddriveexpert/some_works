create or replace view Contracts_and_Actors as
	select id_actor, id_movi, id_contract, number_of_contract, date_contract, id_studio 
from (((actors inner join contracts using (id_actor)) 
inner join film_studios using (id_studio)) 
inner join person on (id_actor = person.id_person))


create or replace view Studio_and_City as
select id_studio, name_of_studio, city from
(city inner join film_studios using (id_city))


create or replace view Movi_and_Country as
select * from (country inner join movies using (id_country))