CREATE DATABASE 'portfolio-database';

CREATE TABLE 'reviews' (
  'id' varchar NOT NULL,
  'user_id' varchar(22) NOT NULL,
  'business_id' varchar(22) NOT NULL,
  'stars' int,
  'useful' int,
  'funny' int,
  'cool' int,
  'text' varchar(500),
  'date' date,
  PRIMARY KEY ('id')
);

CREATE TABLE 'business' (
  'business_id' varchar(22) NOT NULL,
  'name' varchar(255) NOT NULL,

  'id' varchar NOT NULL,
  'user_id' varchar(22) NOT NULL,
  'stars' int,
  'useful' int,
  'funny' int,
  'cool' int,
  'text' varchar(500),
  'date' date,
  PRIMARY KEY ('business_id')
);

