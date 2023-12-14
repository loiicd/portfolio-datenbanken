DROP DATABASE IF EXISTS portfoliodatabase;

CREATE DATABASE portfoliodatabase;

USE portfoliodatabase;

CREATE TABLE business (
  business_id   varchar(22)   NOT NULL,
  name          varchar(255)  NOT NULL,
  address       varchar(255),
  city          varchar(255),
  state         varchar(255),
  postal_code   varchar(255),
  latitude      varchar(255),
  longitude     varchar(255),
  stars         float,
  review_count  int,
  is_open       boolean,
  hours_0       varchar(11),
  hours_1       varchar(11),
  hours_2       varchar(11),
  hours_3       varchar(11),
  hours_4       varchar(11),
  hours_5       varchar(11),
  hours_6       varchar(11),
  PRIMARY KEY (business_id)
);

CREATE TABLE user (
  user_id       varchar(25)  NOT NUll,
  name          varchar(255),
  review_count  int,
  yelping_since date,
  useful        int,
  funny         int,
  cool          int,
  fans          int,
  PRIMARY KEY (user_id)
);

CREATE TABLE review (
  review_id   varchar(22)   NOT NULL,
  user_id     varchar(22)   NOT NULL,
  business_id varchar(22)   NOT NULL,
  stars       int,
  useful      int,
  funny       int,
  cool        int,
  text        varchar(500),
  date        date,
  PRIMARY KEY (review_id),
  FOREIGN KEY (business_id) REFERENCES business(business_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE category (
  category_id varchar(22)   NOT NULL,
  name        varchar(40)   NOT NULL,
  PRIMARY KEY (category_id)
);

CREATE TABLE business_has_category (
  business_id varchar(22)   NOT NULL,
  category_id varchar(22)   NOT NULL,
  CONSTRAINT pk_business_category PRIMARY KEY (business_id, category_id),
  FOREIGN KEY (business_id) REFERENCES business(business_id),
  FOREIGN KEY (category_id) REFERENCES category(category_id)
);

CREATE TABLE user_has_friend (
  first_user_id   varchar(22) NOT NULL,
  second_user_id  varchar(22) NOT NULL,
  CONSTRAINT pk_user_friends PRIMARY KEY (first_user_id, second_user_id),
  FOREIGN KEY (first_user_id) REFERENCES user(user_id),
  FOREIGN KEY (second_user_id) REFERENCES user(user_id)
);