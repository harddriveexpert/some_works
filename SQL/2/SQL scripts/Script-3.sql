create group film_studio_group with login;
grant select, update, insert on contracts to film_studio_group;
grant select, update, insert on actors to film_studio_group;
grant select, update, insert on actor_s_role to film_studio_group;


create group actors_group with login;
grant select on film_studios to actors_group;
grant select on city to actors_group;
grant select on movies to actors_group;
grant select on directors to actors_group;

create group user_group with login;
grant select on country to user_group;
grant select on movies to user_group;
grant select on directors to user_group;

create user film_studio_user with password '1234' login;
    grant film_studio_group to film_studio_user;

create user actors_user with password '1234' login;
    grant actors_group to actors_user;
   
create user user_user with password '1234' login;
    grant user_group to user_user;
   
drop user user_user;
drop user actors_user;
drop user film_studio_user;