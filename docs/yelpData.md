# YelpData

Inhalt:
1. [Setup](#setup)
2. [Data](#data)
    1. [Business](#business)
    2. [Checkin](#checkin)
    3. [Tip](#tip)
    4. [Review](#review)

## Setup

Unter src/yelpData müssen die 5 Yelp Dateien von [Moodle](https://moodle.loerrach.dhbw.de/moodle/course/view.php?id=12391) abgelegt werden. Diese werden nicht mit auf das Repo gepusht, sondern nur lokal abgespeichert.

## Data

### Business

**Filename:** yelp_acedemic_dataset_business.json

**Type:** JSON

| Field        | Datatype | Example                  | Description                                                          |
| ------------ | -------- | ------------------------ | -------------------------------------------------------------------- |
| business_id  | string   | Pns2l4eNsfO8kk83dixA6A   | Unique identifier for the business                                   |
| name         | string   | Abby Rappoport, LAC, CMQ | Name of the business                                                 |
| address      | string   | 1616 Chapala St, Ste 2   | Street address of the business                                       |
| city         | string   | Santa Barbara            | City where the business is located                                   |
| state        | string   | CA                       | State where the business is located                                  |
| postal_code  | string   | 93101                    | Postal code of the business location                                 |
| latitude     | float    | 34.4266787               | Latitude coordinate of the business location                         |
| longitude    | float    | -119.7111968             | Longitude coordinate of the business location                        |
| stars        | float    | 5.0                      | Average star rating of the business                                  |
| review_count | integer  | 7                        | Number of reviews for the business                                   |
| is_open      | integer  | 0                        | Indicator of whether the business is open (1 for open, 0 for closed) |
| attributes   | object   | ...                      | Additional attributes or features of the business                    |
| categories   | string   | Doctors, Nutritionists   | Categories or tags associated with the business                      |
| hours        | object   | ...                      | Business hours information                                           |

### Checkin

**Filename:** yelp_acedemic_dataset_checkin.json

**Type:** JSON

| Field        | Datatype | Example                                  | Description                        |
| ------------ | -------- | ---------------------------------------- | ---------------------------------- |
| business_id  | string   | Pns2l4eNsfO8kk83dixA6A                   | Unique identifier for the business |
| date         | string   | 2010-04-17 21:07:32, 2010-08-07 02:00:36 | Date and time of the checkins      |

### Tip

**Filename:** yelp_acedemic_dataset_tip.json

**Type:** JSON

| Field            | Datatype | Example                | Description                        |
| ---------------- | -------- | ---------------------- | ---------------------------------- |
| user_id          | string   | AGNUgVwnZUey3gcPCJ76iw | Unique identifier for the user     |
| business_id      | string   | Pns2l4eNsfO8kk83dixA6A | Unique identifier for the business |
| text             | string   | Drews Brews = yum!     | Text of the tip                    |
| date             | datetime | 2017-09-30 22:39:11    | Date of the tip                    |
| compliment_count | integer  | 2                      | Number of compliments              |

### Review

**Filename:** yelpReviews.yelpReviews.json

**Type:** JSON

| Field            | Datatype | Example                | Description                        |
| ---------------- | -------- | ---------------------- | ---------------------------------- |
| _id              | object   | ...                    |                                    |
| user_id          | string   | AGNUgVwnZUey3gcPCJ76iw | Unique identifier for the user     |
| business_id      | string   | Pns2l4eNsfO8kk83dixA6A | Unique identifier for the business |
| stars            | integer  | 0                      | Number of stars                    |
| useful           | integer  | 3                      | Number of usefull                  |
| funny            | integer  | 2                      | Number of funny                    |
| cool             | integer  | 1                      | Number of cool                     |
| text             | string   | It is cool             | Text of the Review                 |
| date             | datetime | 2017-09-30 22:39:11    | Date of the Review                 |
