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
  PRIMARY KEY (business_id)
);

CREATE TABLE reviews (
  review_id   varchar(22)   NOT NULL,
  -- user_id     varchar(22)   NOT NULL,
  business_id varchar(22)   NOT NULL,
  stars       int,
  useful      int,
  funny       int,
  cool        int,
  text        varchar(500),
  date        date,
  PRIMARY KEY (review_id),
  FOREIGN KEY (business_id) REFERENCES business(business_id)
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