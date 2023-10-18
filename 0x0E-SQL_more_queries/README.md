# SQL - More queries 
## Description 
This repo is about SQL and MySQL. All the files were executed on Ubuntu 20.04 LTS using MySQL 8.0.

### What is MySQL ?
MySQL is a database management system (DBMS).

A Databse is a systematic collection of data.

### What is SQL ?
SQL stands for Structured Query Langguage. It's a way we use to query a database.

Exemple :
```sql
-- Lists all databases of your MySQL server.
SHOW DATABASES;
```

## Usage
For using these scripts you have have MySQL install.
And :
```
cat scirpt_name.sql | mysql -hlocalhost -uroot -p
```
Or add the database name as argument for the script that need it
```
cat scirpt_name.sql | mysql -hlocalhost -uroot -p database_name
```
