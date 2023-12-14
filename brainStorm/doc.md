# Doc

## Database Setup

### 1. Run Docker 

```bash
docker run --name database-portfolio-mysql -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -d mysql:latest

docker run --name database-portfolio-myadmin -d --link database-portfolio-mysql:db -p 8080:80 phpmyadmin
```

### 2. 

## Database Aufbau

| Field            | Datatype |
| ---------------- | -------- |
| _id              | object   |
| user_id          | string   |
| business_id      | string   |
| stars            | integer  |
| useful           | integer  |
| funny            | integer  |
| cool             | integer  |
| text             | string   |
| date             | datetime |