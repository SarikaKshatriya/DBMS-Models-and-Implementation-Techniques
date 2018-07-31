# DBMS-Models-and-Implementation-Techniques
Project 2:

To implement a program that helps to learn usage of MongoDB as an example of a document-oriented NOSQL system, and see how data is stored and queried in such a system.
Programing Language:  Python2.7
Database:  MongoDB, Mysql
Data structures used in Python:  List, Dictionary

Table of Contents

1.Loaded data in Mysql	1
i.  employee table:	1
ii. project table:	2
iii. department table:	3
iv. works_on table:	4
v.dept_locations table:	5
2.PROJECT document:	6
3.DEPARTMENT document:	7
4.Pseudo code:	9
5.Mongodb installation:	10
  
1.Loaded data in Mysql

We have created tables for each given input text files and loaded data into respective tables in Mysql. All tables are created under the schema “company”.
i.  employee table:
Created table employee in Mysql with the following query-
create table company.employee
(Fname varchar(20),
 Minit varchar(3),
 Lname varchar(20),
 Ssn int(20),
 Bdate varchar(20),
 Address varchar(30),
 Sex varchar(2),
 Salary int(5),
 Super_ssn int(20),
 Dno int(5));
Loaded data from employee.txt file to employee table with the following query-
LOAD DATA LOCAL INFILE 'C:/Users/rosha/Desktop/DB2/employee.txt' INTO TABLE company.employee FIELDS TERMINATED BY ', ' OPTIONALLY ENCLOSED BY '"'LINES TERMINATED BY '\n';
 
ii. project table:

Created table project in Mysql with the following query:
create table company.project
(Pname varchar(15),
 Pnumber int(5),
 Plocation varchar(25),
 Dnum int(5));
Loaded data from project.txt file to project table with the following query-
LOAD DATA LOCAL INFILE 'C:/Users/rosha/Desktop/DB2/project.txt' INTO TABLE company.project FIELDS TERMINATED BY ', ' OPTIONALLY ENCLOSED BY '"'LINES TERMINATED BY '\n';
 

iii. department table:

Created table department in Mysql with the following query:
create table company.department
(Dname varchar(15),
 Dnumber int(5),
 Mgr_ssn int(20),
 Mgr_start_date varchar(20));
Loaded data from department.txt file to department table with the following query:
LOAD DATA LOCAL INFILE 'C:/Users/rosha/Desktop/DB2/ department.txt' INTO TABLE company. department FIELDS TERMINATED BY ', ' OPTIONALLY ENCLOSED BY '"'LINES TERMINATED BY '\n';
 


iv. works_on table:

Created table works_on in Mysql with the following query:
create table company.works_on
(Essn int(20),
 Pno int(5),
 Hours decimal(3,1));
Loaded data from Works_on.txt file to works_on table with the following query:
LOAD DATA LOCAL INFILE 'C:/Users/rosha/Desktop/DB2/ Works_on.txt' INTO TABLE company. works_on FIELDS TERMINATED BY ', ' OPTIONALLY ENCLOSED BY '"'LINES TERMINATED BY '\n';
 


v.dept_locations table:

Created table dept_locations in Mysql with the following query:
create table company.dept_locations
(Dnumber int(5),
 Dlocation varchar(20));
Loaded data from dept_Locations.txt file to dept_locations table with the following query-
LOAD DATA LOCAL INFILE 'C:/Users/rosha/Desktop/DB2/ dept_locations.txt.txt' INTO TABLE company. dept_locations.txt FIELDS TERMINATED BY ', ' OPTIONALLY ENCLOSED BY '"'LINES TERMINATED BY '\n';
 

We will design two document (complex object) schemas in mongodb, corresponding to given data:
2.PROJECT document:

This document will include the following data with the respective files: Pnumber, Pname, Dname (of the controlling department), plus a list of the employees that work on the project {employees: Lname, Fname, Hours}.
Project:Pnumber,Pname
Department:Dname
Employees: Lname, Fname
Works_on:Hours

To get this document, we have created the result table, company.project_data and used the following query to join the 4 tables and insert data in project_data table.
  The following query creates table project_data table:
  create table company.project_data
(Pnumber int(5),
 Pname varchar(15),
 Dname varchar(15),
 Lname varchar(20),
 Fname varchar(20),
 Hours decimal(3,1));

Insert into company.project_data
select p.Pnumber,p.Pname,d.Dname,e.Lname,e.Fname,w.Hours
from   department d,employee e,works_on w,project p
where  d.Dnumber=p.Dnum and e.ssn=w.Essn and p.Pnumber=w.Pno
order by p.Pnumber;


 
3.DEPARTMENT document: 

This document will include the following data from the respective files: Dname, the department manager’s Lname, and a list of the locations of the department {locations: Dlocation}
Department: Dname
Employee: Lname
Project: Dlocation

To get this document, , we have created the result table, company.department_data and we have used the following query to join the 3 tables and saving the data in department_data table.

The following query creates table department_data table:
  create table company.department_data
(Dnumber int(5),
 Dname varchar(15),
 Lname varchar(20),
 Dlocation varchar(15));


Insert into company.department_data
select d.Dnumber,d.Dname,e.Lname,e.Fname,l.Dlocation
from department d,employee e,dept_locations l
where d.Mgr_ssn=e.ssn
and l.Dnumber=d.Dnumber
order by d.Dnumber;

 


4.Pseudo code (Updated)

1.Import all the necessary libraries like json, pandas, pymongo, pymsql, collections
2. Connect to mongodb in localhost.
conn = pymongo.MongoClient("mongodb://localhost")
3.Create database company.
db=conn.company
4. create collection project
record = db.project
5.Open project.json file and read json data.
file = open("project.json", 'r')
parsed = json.loads(file1.read())
6.Insert json data to mongodb project collection.
for item in parsed1["prjDetails"]:
    record.insert(item)
    
5. create collection department

record = db. department
5.Open department.json file and read json data.
file = open("department.json", 'r')
parsed = json.loads(file1.read())
6.Insert json data to mongodb department collection.
for item in parsed1["DeptDetails"]:
    record.insert(item)




5.Mongodb installation:
We have installed mongodb and created one document with name student. This collection contains two fields name and utaid. We have added two records using insert and fetched data using find command.
The following images shows the commands used to create, insert and fetch data from student document.

 


 
We have also installed Robo 3T (mongodb management tool). It shows the created collection and inserted data.
 

