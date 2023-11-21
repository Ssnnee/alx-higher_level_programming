# 0x0F. Python - Object-relational mapping

This project cover Databases and Python.
In the first part, we use MySQLdb to connect a MySQL database and execute MySQl
queries
In the second part, we use SQLAlchemy wich is an Obejct Relational Mapper (ORM)
The difference between those two is : no SQL querie!

### Usage
To use the script, you have have the database and use it like this for most of
the file :
- Use the sql file to create the database by piping it to mysql
- Then just have to run the script with appropriate argument. Mostly the argument
will be `USER, PASSWORD, DATABASE `
* Exempale
```
$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```
