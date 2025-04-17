OPTIONS (SKIP=1)
load data
infile 'myterror.csv'
insert into table myterror
fields terminated by ','
trailing nullcols(
    event_id,
    iyear,
    imonth,
    iday,
    country,
    country_txt,
    region,
    region_txt,
    provstate,
    city,
    latitude,
    longitude
)
