create table mida (
dispnum3 int,
dispnum4 int,
stday int,
stmon int,
styear int,
endday int,
endmon int,
endyear int,
outcome int,
settle int,
fatality int,
fatalpre int,
maxdur int,
mindur int,
hiact int,
hostlev int,
recip int,
numa int,
numb int,
link1 varchar,
link2 varchar,
link3 varchar,
ongo2010 boolean,
version double precision);

create table midb (
dispnum3 int,
dispnum4 int,
stabb varchar(3),
ccode int,
stday int,
stmon int,
styear int,
endday int,
endmon int,
endyear int,
sidea int,
revstate int,
revtype1 int,
revtype2 int,
fatality int,
fatalpre int,
hiact int,
hostlev int,
orig int,
version double precision
);

create table midi (
dispnum3 int,
incidnum3 int,
dispnum4 int,
incidnum4 int,
stday int,
stmon int,
styear int,
endday int,
endmon int,
endyear int,
duration int,
tbi int,
fatality int,
fatalpre int,
action int,
hostlev int,
numa int,
revtype1 int,
revtype2 int,
version double precision
);

create table midp (
dispnum3 int,
incidnum3 int,
dispnum4 int,
incidnum4 int,
stabb varchar(3),
ccode int,
stday int,
stmon int,
styear int,
endday int,
endmon int,
endyear int,
insidea int,
sidea int,
fatality int,
fatalpre int,
action int,
hostlev int,
revtype1 int,
revtype2 int,
version double precision
);

select * from mida where dispnum3 = 1549;

delete from mida where dispnum3 = 1549;

insert into mida values
(1549, -9, 2, 3, 1860, 20, 3, 1860, 5, 3, -9, -9, 19, 19, 17, 4, 1, 1, 1, 0, 0, 0, false, 4.3000002);

--delete from mida;

alter table mida 
add primary key (dispnum3);

--delete from midb;

--delete from midi;

--delete from midp;

alter table midb
add column id serial primary key;

alter table midb
add constraint fk_dispnum3 foreign key (dispnum3)
references mida (dispnum3);

select * from mida where stabb='RUS' or stabb='USR';
select * from midb where stabb='RUS' or stabb='USR';
select * from midp where stabb='RUS' or stabb='USR';

--update midb set stabb = case when stabb = 'USR' then 'RUS' end;

alter table midb
add constraint fk_stabb foreign key (stabb)
references cow_country_codes (stateabb);

alter table midb
add constraint fk_ccode foreign key (ccode)
references cow_country_codes (ccode);

alter table midi add primary key (incidnum3);

alter table midi add constraint fk_dispnum3
foreign key (dispnum3)
references mida (dispnum3);

insert into mida (dispnum3) values (4157);

alter table midp add primary key (incidnum3, ccode);

alter table midp
add constraint fk_incidnum3 foreign key (incidnum3)
references midi (incidnum3);

alter table midp add constraint fk_ccode foreign key (ccode)
references cow_country_codes (ccode);

alter table midp add constraint fk_dispnum3 foreign key (dispnum3)
references mida (dispnum3);

select region from regions
union select region from wrp_regional;

select region from wrp_regional;

--update midb set stabb = case when stabb = 'USR' then 'RUS' end;

select * from wrp_regional;
delete from wrp_regional;

alter table regions
add constraint unique_region unique (region);

alter table wrp_regional 
add constraint fk_region foreign key (region)
references regions (region);

create table midloca (
year int,
dispnum	int,
midloc2_location varchar,
midloc2_measuringpoint varchar,
midloc2_xlongitude double precision,
midloc2_ylatitude double precision,
midloc2_precision int,
midloc2_howobtained varchar,
midloc2_precision_comment varchar,
midloc2_general_comment	varchar,
priogrid_cell int,
midloc11_location varchar,
midloc11_midlocmeasuringpoint varchar,
midloc11_latitude double precision,
midloc11_longitude double precision,
midloc11_precision int
);

select * from midloca;

alter table midloca
add primary key (dispnum);

alter table midloca 
add constraint fk_dispnum foreign key (dispnum)
references mida (dispnum3);

create table midloci (
year int,
dispnum	int,
incidnum int,
midloc2_location varchar,
midloc2_measuringpoint varchar,
midloc2_xlongitude double precision,
midloc2_ylatitude double precision,
midloc2_precision int,
onset boolean,
midloc2_howobtained varchar,
midloc2_precision_comment varchar,
midloc2_general_comment	varchar,
priogrid_cell int,
midloc11_location varchar,
midloc11_midlocmeasuringpoint varchar,
midloc11_latitude double precision,
midloc11_longitude double precision,
midloc11_precision int);

alter table midloci
add primary key (incidnum);

alter table midloci 
add constraint fk_incidnum foreign key (incidnum)
references midi (incidnum3);

alter table midloci
add constraint fk_dispnum foreign key (dispnum)
references mida (dispnum3);

drop table nmc;
create table nmc (
stateabb varchar(3),
ccode int,
year int,
milex int,
milper int,
irst int,
pec int,
tpop double precision,
upop double precision,
cinc double precision,
version int
);

alter table nmc add primary key (ccode, year);
alter table nmc add constraint fk_ccode foreign key (ccode)
references cow_country_codes (ccode);
alter table nmc add constraint fk_stateabb foreign key (stateabb)
references cow_country_codes (stateabb);
alter table nmc rename to nmc5;

create table alliance_by_member (
version4id int,
ccode int references cow_country_codes(ccode),
state_name varchar,
all_st_day int,
all_st_month int,
all_st_year int,
all_end_day int,
all_end_month int,
all_end_year int,
ss_type varchar,
mem_st_day int,
mem_st_month int,
mem_st_year int,
mem_end_day	int,
mem_end_month int,
mem_end_year int,
left_censor boolean,
right_censor boolean,
defense	boolean,
neutrality boolean,
nonaggression boolean,
entente	boolean,
version double precision,
primary key (version4id, ccode, mem_st_day, mem_st_month, mem_st_year)
);

create table alliance_by_member_yearly (
version4id int,
ccode int references cow_country_codes(ccode),
state_name varchar,
all_st_day int,
all_st_month int,
all_st_year int,
all_end_day int,
all_end_month int,
all_end_year int,
ss_type varchar,
mem_st_day int,
mem_st_month int,
mem_st_year int,
mem_end_day	int,
mem_end_month int,
mem_end_year int,
left_censor boolean,
right_censor boolean,
defense	boolean,
neutrality boolean,
nonaggression boolean,
entente	boolean,
year int,
version double precision,
primary key (version4id, ccode, year));

create table alliance_by_directed (
version4id int,
ccode1 int references cow_country_codes(ccode),
state_name1	varchar,
ccode2 int references cow_country_codes(ccode),
state_name2	varchar,
dyad_st_day int,
dyad_st_month int,
dyad_st_year int,
dyad_end_day int,
dyad_end_month int,
dyad_end_year int,
left_censor boolean,
right_censor boolean,
defense	boolean,
neutrality boolean,
nonaggression boolean,
entente boolean,
version double precision);

create table alliance_by_directed_yearly (
version4id int,
ccode1 int references cow_country_codes (ccode),
state_name1	varchar,
ccode2 int references cow_country_codes (ccode),
state_name2	varchar,
dyad_st_day	int,
dyad_st_month int,
dyad_st_year int,
dyad_end_day int,
dyad_end_month int,
dyad_end_year int,
left_censor boolean,
right_censor boolean,
defense	boolean,
neutrality boolean,
nonaggression boolean,
entente boolean,
year int,
version double precision
);

drop table alliance_by_dyad;
create table alliance_by_dyad (
version4id int,
ccode1 int references cow_country_codes (ccode),
state_name1	varchar,
ccode2 int references cow_country_codes (ccode),
state_name2	varchar,
dyad_st_day	int,
dyad_st_month int,
dyad_st_year int,
dyad_end_day int,
dyad_end_month int,
dyad_end_year int,
left_censor boolean,
right_censor boolean,
defense	boolean,
neutrality boolean,
nonaggression boolean,
entente boolean,
asymetric boolean,
version double precision
);

create table alliance_by_dyad_yearly (
version4id int,
ccode1 int references cow_country_codes (ccode),
state_name1	varchar,
ccode2 int references cow_country_codes (ccode),
state_name2	varchar,
dyad_st_day	int,
dyad_st_month int,
dyad_st_year int,
dyad_end_day int,
dyad_end_month int,
dyad_end_year int,
left_censor boolean,
right_censor boolean,
defense	boolean,
neutrality boolean,
nonaggression boolean,
entente boolean,
year int,
version double precision
);

create table contdir (
dyad int,
statelno int references cow_country_codes (ccode),
statelab varchar(3) references cow_country_codes (stateabb),
statehno int references cow_country_codes (ccode),
statehab varchar(3) references cow_country_codes (stateabb),
conttype int,
begin_month int,
end_month int,
notes varchar,
version double precision
);

create table contdird (
dyad int,
state1no int references cow_country_codes (ccode),
state1ab varchar(3) references cow_country_codes (stateabb),
state2no int references cow_country_codes (ccode),
state2ab varchar(3) references cow_country_codes (stateabb),
year int,
conttype int,
version double precision
);

create table contdirs (
stateno	int references cow_country_codes (ccode),
stateab	varchar(3) references cow_country_codes (stateabb),
year int,
total int,
land int,
sea int,
version double precision	
);

drop table territorial_change_data;
create table territorial_change_data (
year int,
month int,
gainer int,
gaintype int,
procedur int,
entity int,
contgain int,
area double precision,
pop int,
portion	int,
loser int,
losetype int,
contlose int,
entry int,
exit int,
number int,
indep int,
conflict int,
version double precision
);

insert into cow_country_codes
values ('unk',-9,'Unknown');

select * from cow_country_codes;

select * from system2016;

create table contcol (
dyad int,
statelno int references cow_country_codes (ccode),
statelab varchar(3) references cow_country_codes (stateabb),
dependl int,
conttype int,
statehno int references cow_country_codes (ccode),
statehab varchar(3) references cow_country_codes (stateabb),
dependh	int,
begin_year int,
end_year int,
version double precision
);

create table contcold (
dyad int,
statelno int references cow_country_codes (ccode),
statelab varchar(3) references cow_country_codes (stateabb),
statehno int references cow_country_codes (ccode),
statehab varchar(3) references cow_country_codes (stateabb),
year int,
land int,
sea	int,
total int,
version double precision
);

create table contcols (
stateno	int references cow_country_codes (ccode),
stateab	varchar(3) references cow_country_codes (stateabb),
year int,
total int,
land int,
sea int,
version double precision
);