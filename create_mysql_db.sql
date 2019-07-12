drop database cow;
create database if not exists cow;
use cow;

create table if not exists country_codes (
id INT AUTO_INCREMENT NOT NULL,
StateAbb VARCHAR(3) NOT NULL,
CCode SMALLINT UNSIGNED NOT NULL,
StateNme VARCHAR(60) NOT NULL,
PRIMARY KEY (id)
);

create table if not exists states2016 (
id INT AUTO_INCREMENT NOT NULL,
stateabb VARCHAR(3) NOT NULL,
ccode SMALLINT UNSIGNED NOT NULL,
statenme VARCHAR(60),
styear SMALLINT,
stmonth TINYINT,
stday TINYINT,
endyear SMALLINT,
endmonth TINYINT,
endday TINYINT,
version INT,
PRIMARY KEY (id)
);

select * from states2016;

create table if not exists majors_2016 (
id INT AUTO_INCREMENT NOT NULL,
stateabb VARCHAR(3) NOT NULL,
ccode SMALLINT UNSIGNED NOT NULL,
styear SMALLINT,
stmonth TINYINT,
stday TINYINT,
endyear SMALLINT,
endmonth TINYINT,
endday TINYINT,
version SMALLINT,
PRIMARY KEY (id)
);

create table if not exists MIDIP_4_3 (
id INT AUTO_INCREMENT,
dispnum3 INT,
incidnum3 INT,
dispnum4 INT,
incidnum4 INT,
stabb VARCHAR(3),
ccode SMALLINT UNSIGNED NOT NULL,
stday TINYINT,
stmon TINYINT,
styear SMALLINT,
endday TINYINT,
endmon TINYINT,
endyear SMALLINT,
insidea TINYINT,
sidea TINYINT,
fatality TINYINT,
fatalpre INT,
action TINYINT,
hostlev TINYINT,
revtype1 TINYINT,
revtype2 TINYINT,
version FLOAT,
PRIMARY KEY (id)
);

create table if not exists cow_war_list (
year SMALLINT NOT NULL,
war_name VARCHAR(280) NOT NULL,
war_type_number VARCHAR(32) UNIQUE NOT NULL,
PRIMARY KEY (war_type_number)
);

create table if not exists MIDA_4_3 (
id INT AUTO_INCREMENT NOT NULL,
dispnum3 INT NOT NULL,
dispnum4 INT NOT NULL,
stday TINYINT,
stmon TINYINT,
styear SMALLINT,
endday TINYINT,
endmon TINYINT,
endyear SMALLINT,
outcome TINYINT,
settle TINYINT,
fatality TINYINT,
fatalpre INT,
maxdur INT,
mindur INT,
hiact TINYINT,
hostlev TINYINT,
recip TINYINT,
numa TINYINT,
numb TINYINT,
link1 INT,
link2 INT,
link3 INT,
ongo2010 TINYINT,
version FLOAT,
PRIMARY KEY (id)
);

create table if not exists MIDB_4_3 (
id INT AUTO_INCREMENT NOT NULL,
dispnum3 INT NOT NULL,
dispnum4 INT NOT NULL,
stabb VARCHAR(3) NOT NULL,
ccode SMALLINT UNSIGNED NOT NULL,
stday TINYINT,
stmon TINYINT,
styear SMALLINT,
endday TINYINT,
endmon TINYINT,
endyear SMALLINT,
sidea TINYINT,
revstate TINYINT,
revtype1 TINYINT,
revtype2 TINYINT,
fatality TINYINT,
fatalpre INT,
hiact SMALLINT,
hostlev TINYINT,
orig TINYINT,
version FLOAT,
PRIMARY KEY (id)
);

create table if not exists MIDI_4_3 (
id INT AUTO_INCREMENT NOT NULL,
dispnum3 INT NOT NULL,
incidnum3 INT NOT NULL,
dispnum4 INT NOT NULL,
incidnum4 INT NOT NULL,
stday TINYINT,
stmon TINYINT,
styear SMALLINT,
endday TINYINT,
endmon TINYINT,
endyear SMALLINT,
duration INT,
tbi INT,
fatality TINYINT,
fatalpre INT,
action INT,
hostlev TINYINT,
numa INT,
revtype1 INT,
revtype2 INT,
version FLOAT,
PRIMARY KEY (id)
);

create table if not exists midloci_2_0 (
id INT UNSIGNED AUTO_INCREMENT NOT NULL,
year SMALLINT,
dispnum INT,
incidnum INT,
midloc2_location VARCHAR(280),
midloc2_measuringpoint VARCHAR(280),
midloc2_xlongitude FLOAT NOT NULL,
midloc2_ylatitude FLOAT NOT NULL,
midloc2_precision INT,
onset TINYINT,
midloc2_howobtained VARCHAR(280),
midloc2_precision_comment VARCHAR(280),
midloc2_general_comment VARCHAR(280),
priogrid_cell INT,
midloc11_location VARCHAR(280),
midloc11_midlocmeasuringpoint VARCHAR(280),
midloc11_latitude FLOAT,
midloc11_longitude FLOAT,
midloc11_precision INT,
PRIMARY KEY (id)
);

create table if not exists midloca_2_0 (
id INT UNSIGNED AUTO_INCREMENT NOT NULL,
year SMALLINT,
dispnum INT,
midloc2_location VARCHAR(280),
midloc2_measuringpoint VARCHAR(280),
midloc2_xlongitude FLOAT NOT NULL,
midloc2_ylatitude FLOAT NOT NULL,
midloc2_precision INT,
midloc2_howobtained VARCHAR(280),
midloc2_precision_comment VARCHAR(280),
midloc2_general_comment VARCHAR(280),
priogrid_cell INT,
midloc11_location VARCHAR(280),
midloc11_midlocmeasuringpoint VARCHAR(280),
midloc11_latitude FLOAT,
midloc11_longitude FLOAT,
midloc11_precision INT,
PRIMARY KEY (id)
);