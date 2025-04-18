use testdb;

create table `users` (
    `id` varchar(120) not null,
    `nickname` varchar(20) default null,
    `email` varchar(20) default null,
    `phone` varchar(20) default null,
    `description` varchar(20) default null,
    primary key (`id`)
) engine = InnoDB default charset = utf8mb4
collate = utf8mb4_0900_ai_ci
