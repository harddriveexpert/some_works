select * from (select id_actor, name_of_studio from 
((actors inner join contracts using (id_actor)) 
inner join film_studios using (id_studio))) as step1 
inner join person on (step1.id_actor = id_person) 
where step1.name_of_studio = 'Emelda'

with step1 as (select * from ((movies inner join contracts using (id_movi)) 
inner join actors using (id_actor)))
select step1.id_actor, step1.name_of_movi from step1, actors 
where step1.id_actor != actors.id_actor


select * from (select id_actor, name_of_studio, number_of_contract from 
((actors inner join contracts using (id_actor)) 
inner join film_studios using (id_studio))) as step1 
inner join person on (step1.id_actor = id_person) 
where step1.name_of_studio = 'Emelda' as step2


select name_of_studio from ((((film_geners_movies 
inner join film_genres using (id_ganre))
inner join movies using (id_movi)) 
inner join contracts using (id_movi))
inner join film_studios using (id_studio)) 
where (ganre_name = 'Horror') and (date_movi = 1997)

select * from ((((actors inner join contracts using (id_actor)) 
inner join film_studios using (id_studio))) 
inner join city using(id_city)) as step1
inner join person on (step1.id_actor = id_person)
where step1.id_city = person.id_city





