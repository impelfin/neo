use testdb;

create table user(userid char(8), passwd char(8)) default charset=utf8;

show tables;

alter table user add constraint pk_userid primary key(userid);

explain user;

insert into user values('root', '1234');

select * from user;
