use st_db;
select st_info.NAME, st_info.DEPT, st_grade.Linux, st_grade.DB from st_info, st_grade where st_info.ST_ID = 202501 and st_grade.ST_ID=202501;
