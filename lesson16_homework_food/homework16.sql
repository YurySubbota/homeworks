create database lesson16_hw_food owner subbota encoding='utf8'

CREATE TABLE users (
    id primary key integer,--The id field cannot be empty, it must contain a unique integer
    name not null varchar);--the name field cannot be empty, it must contain text information

create table eating (
    id primary key integer,--The id field cannot be empty, it must contain a unique integer
    when date,--the when field can contain a date and time or null
    who not null integer,--the who field cannot be empty, it must contain the id of the person who ate
    what not null integer);--the what field cannot be empty, it must contain the id of what you ate

create table product (
    id not null unique integer--The id field cannot be empty, it must contain a unique integer
    name_of_product varchar);--The name_of_product field can contain the product name