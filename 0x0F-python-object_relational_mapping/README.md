# 0x0F. Python - Object-relational mapping

This project cover Databases and Python.
In the first part, we use MySQLdb to connect a MySQL database and execute MySQl
queries
In the second part, we use SQLAlchemy wich is an Obejct Relational Mapper (ORM)
The difference between those two is : no SQL querie!

### Usage
To use the script, you have have the database and use it like this for most of
the file :
```shell
./0-file_name.py root root hbtn_0e_0_usa
```
You can use this to create the database :

- Create a sql file. Example `sql_file.js`

```sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
```

- Then you just have to pip the script into mysql
```shell
cat sql_file.js | mysql -uroot -p
```
