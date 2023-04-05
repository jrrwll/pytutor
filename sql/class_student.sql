-- create database jk;
-- use jk;

create table class (
    id bigint not null auto_increment primary key, name varchar(255) not null comment '名称'
) engine=innodb default charset=uft8mb4 comment=''班级'';

create table student (
    id       bigint       not null auto_increment primary key,
    name     varchar(255) not null comment '姓名',
    age      smallint comment '年龄',
    gender   varchar(255) comment '性别',
    number   varchar(255) comment '学号',
    class_id bigint       not null comment '班级ID'
) engine=innodb default charset=uft8mb4 comment='学生';

create table score (
    id           bigint       not null auto_increment primary key,
    student_name bigint       not null comment '学生ID',
    subject      varchar(255) not null comment '科目',
    value        smallint comment '分数',
) engine=innodb default charset=uft8mb4 comment='成绩';

-- 

insert into class (id, name)
values (1, '1401');

insert into score (id, student_name, subject, value)
values (1, 'jk', 'math', 99),
       (2, 'zh', 'math', 69),
       (3, 'cl', 'math', 33),
       (4, 'lg', 'math', 60),
       (5, 'jk', 'chinese', 68),
       (6, 'zh', 'chinese', 86),
       (7, 'cl', 'chinese', 91),
       (8, 'lg', 'chinese', 55);

insert into student (id, name, age, gender, number, class_id)
values (1, 'jk', 17, 'male', '411', 1),
       (2, 'lg', 18, 'female', '412', 1),
       (3, 'zh', 25, 'male', '602', 1),
       (4, 'cl', 29, 'female', '303', 1);
