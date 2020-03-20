/* Retrieve MIDA and MIDLOCA data for major powers */
select m.dispnum3, stabb, ccode, x.*
from midp as m
inner join
(select * from midloca
inner join mida
on midloca.dispnum = mida.dispnum3) as x
on m.dispnum3 = x.dispnum3
where m.ccode in 
(select ccode from majors2016)
order by year asc;

select * from alliance_by_dyad_yearly;

