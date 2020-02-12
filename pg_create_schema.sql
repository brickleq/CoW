select * from wrp_national;
/*
ALTER TABLE child_table 
ADD CONSTRAINT constraint_name FOREIGN KEY (c1) REFERENCES parent_table (p1);*/
alter table wrp_national
add constraint fk_state foreign key (state)
references country_codes (ccode);

insert into country_codes values ('NEP',790,'Nepal');
insert into country_codes values ('THI',800,'Thailand');
insert into country_codes values ('CAM',811,'Cambodia');
insert into country_codes values ('MAL',820,'Malaysia');
insert into country_codes values ('INS',850,'Indonesia');
insert into country_codes values ('VAN',935,'Vanuatu');
insert into country_codes values ('FIJ',950,'Fiji');
insert into country_codes values ('PAL',986,'Palau');
insert into country_codes values ('WSM',990,'Samoa');
insert into country_codes values (
('FSM',987,'Federated States of Micronesia'),
('WSM',990,'Samoa')
);

select * from country_codes;
insert into country_codes values ('LAO',812,'Laos');
insert into country_codes values ('DRV',816,'Vietnam');
insert into country_codes values ('RVN',817,'Republic of Vietnam');
insert into country_codes values ('MAL',820,'Malaysia');
insert into country_codes values ('SIN',830,'Singapore');
insert into country_codes values ('BRU',835,'Brunei');
insert into country_codes values ('PHI',840,'Philippines');
insert into country_codes values ('INS',850,'Indonesia');
insert into country_codes values ('ETM',860,'East Timor');
insert into country_codes values ('AUL',900,'Australia');
insert into country_codes values ('PNG',910,'Papua New Guinea');
insert into country_codes values ('NEW',920,'New Zealand');
insert into country_codes values ('VAN',935,'Vanuatu');
insert into country_codes values ('SOL',940,'Solomon Islands');
insert into country_codes values ('KIR',946,'Kiribati');
insert into country_codes values ('TUV',947,'Tuvalu');
insert into country_codes values ('FIJ',950,'Fiji');
insert into country_codes values ('TON',955,'Tonga');
insert into country_codes values ('NAU',970,'Nauru');
insert into country_codes values ('MSI',983,'Marshall Islands');
insert into country_codes values ('PAL',986,'Palau');
insert into country_codes values ('FSM',987,'Federated States of Micronesia');
insert into country_codes values ('SAM',990,'Samoa');

alter table wrp_national
add constraint fk_year foreign key (year)
references wrp_global (year);

alter table states2016
add constraint fk_stateabb foreign key (stateabb)
references country_codes (stateabb);

alter table wrp_regional
alter column sumrelig type bigint;

alter table wrp_regional
add constraint fk_year foreign key (year)
references wrp_global (year);

alter table states2016
add constraint fk_ccode foreign key (ccode)
references country_codes (ccode);

alter table system2016
add constraint fk_ccode foreign key (ccode)
references country_codes (ccode);

select * from wrp_national;

alter table states2016
drop column id;

alter table system2016
add primary key (ccode, year);

select * from system2016;

alter table system2016 add column id serial primary key;

alter table states2016 
add primary key (ccode, styear);

alter table system2016
add constraint fk_ccode foreign key (ccode)
references country_codes (ccode);

alter table system2016
add constraint fk_year foreign key (year)
references states2016 (styear);

alter table majors2016
add constraint fk_ccode foreign key (ccode)
references country_codes (ccode);

drop table inter_state_war_data;

alter table country_codes rename to cow_country_codes;

select * from inter_state_war_data;

alter table inter_state_war_data
alter column "TransFrom" type integer array
USING "TransFrom"::integer[];

alter table inter_state_war_data
drop constraint inter_state_war_data_pkey;

alter table inter_state_war_data
add primary key (id); 
select * from inter_state_war_data;

alter table inter_state_war_data
add constraint fk_ccode foreign key (ccode)
references cow_country_codes (ccode);

create table typology (
war_type_id integer primary key,
war_type varchar
);

insert into typology (war_type_id, war_type) values 
(1, 'Inter-state war'),
(2, 'Extra-state war: Colonial--conflict with colony'),
(3, 'Extra-state war: Imperial--state vs. nonstate'),
(4, 'Intra-state war: Civil war--for central control'),
(5, 'Intra-state war: Civil war--over local issues'),
(6, 'Intra-state war: Regional internal'),
(7, 'Intra-state war: Intercommunal'),
(8, 'Non-state war: In nonstate territory'),
(9, 'Non-state war: Across state borders');

select * from inter_state_war_data;

alter table inter_state_war_data
add constraint fk_wartype foreign key ("WarType")
references typology (war_type_id);

create table cow_war_list (
year int,
war varchar(255),
type varchar,
code int);

select * from cow_war_list;

alter table cow_war_list
add primary key (code);

alter table inter_state_war_data
add constraint fk_warnum foreign key ("WarNum")
references cow_war_list (code);

alter table cow_war_list
rename warnum to war_num;

select * from cow_country_codes;
insert into cow_country_codes (stateabb, ccode, statenme)
values ('N/A',-8,'Not Applicable');

create table intra_state_war_data (
war_num int,
war_name varchar,
war_type int,
ccode_a int,
side_a varchar,
ccode_b int,
side_b varchar,
intnl boolean,
start_month_1 int,
start_day_1 int,
start_year_1 int,
end_month_1 int,
end_day_1 int,
end_year_1 int,
start_month_2 int,
start_day_2 int,
start_year_2 int,
end_month_2 int,
end_day_2 int,
end_year_2 int,
trans_from int,
where_fought int,
initiator varchar,
outcome int,
trans_to int,
side_a_deaths int,
side_b_deaths int,
version double precision);

select * from intra_state_war_data;

alter table intra_state_war_data
add constraint fk_ccode_a foreign key (ccode_a)
references cow_country_codes (ccode);

alter table intra_state_war_data
add constraint fk_ccode_b foreign key (ccode_b)
references cow_country_codes (ccode);

create table regions (
where_fought int primary key,
region varchar);

insert into regions values
(1, 'Western Hemisphere'),
(2, 'Europe'),
(4, 'Africa'),
(6, 'Middle East'),
(7, 'Asia'),
(9, 'Oceania');
select * from regions;

insert into regions values
(11, 'Europe & Middle East'),
(12, 'Europe & Asia'),
(13, 'Western Hemisphere & Asia'),
(14, 'Europe, Africa & Middle East'),
(15, 'Europe, Africa, Middle East & Asia'),
(16, 'Africa, Middle East, Asia & Oceania'),
(17, 'Asia & Oceania'),
(18, 'Africa & Middle East'),
(19, 'Europe, Africa, Middle East, Asia & Oceania');

alter table inter_state_war_data
add constraint fk_where_fought foreign key ("WhereFought")
references regions (where_fought);

alter table intra_state_war_data
add constraint fk_war_type foreign key (war_type)
references typology (war_type_id);

insert into cow_war_list values
(1899, 'Sixth Colombian (War of the 1,000 Days) of 1899-1902', 'Intra-State War', 636);

alter table intra_state_war_data
add constraint fk_war_num foreign key (war_num)
references cow_war_list (war_num);

create table extra_state_war_data (
war_num int,
war_name varchar,
war_type int,
ccode1 int,
side_a varchar,
ccode2 int,
side_b varchar,
start_month_1 int,
start_day_1 int,
start_year_1 int,
end_month_1 int,
end_day_1 int,
end_year_1 int,
start_month_2 int,
start_day_2 int,
start_year_2 int,
end_month_2 int,
end_day_2 int,
end_year_2 int,
initiator int,
interven int,
trans_from int,
outcome int,
trans_to int,
where_fought int,
bat_death int,
nonstate_deaths int,
version double precision
);

select * from extra_state_war_data;

alter table extra_state_war_data
add constraint fk_war_num foreign key (war_num)
references cow_war_list (war_num);

alter table extra_state_war_data
add constraint fk_ccode1 foreign key (ccode1)
references cow_country_codes (ccode);


alter table extra_state_war_data
add constraint fk_ccode2 foreign key (ccode2)
references cow_country_codes (ccode);

alter table extra_state_war_data
add constraint fk_war_type foreign key (war_type)
references typology (war_type_id);

alter table extra_state_war_data
add constraint fk_where_fought foreign key (where_fought)
references regions (where_fought);

select * from extra_state_war_data;

