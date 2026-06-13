CREATE DATABASE IF NOT EXISTS inventory_db;

USE inventory_db;

CREATE TABLE Categories(
category_id int primary key auto_increment,
category_name varchar(50) unique not null
);

CREATE TABLE Suppliers(
suppliers_id int primary key,
suppliers_name varchar(50) unique not null,
contact varchar(50) unique not null,
city varchar(20) not null
);

CREATE TABLE Products(
product_id int primary key auto_increment,
product_name varchar(50) not null,
category_id int,
suppliers_id int,
quantity int,
price int,

foreign key(category_id)
references Categories(category_id),

foreign key(suppliers_id)
references Suppliers(suppliers_id)
);

CREATE TABLE stock_transactions(
transaction_id int primary key,
product_id int,
transaction_type varchar(20) not null,
quantity int,
transaction_date date,

foreign key(product_id)
references Products(product_id)
);

insert into Categories
(category_name)
values("Electronics");

insert into Categories
(category_name)
values("Stationery");

insert into Categories
(category_name)
values("Furniture");

insert into Suppliers
(suppliers_id,suppliers_name,contact,city)
values(101,"Tech Distributors","03001234567","Karachi");

insert into Suppliers
(suppliers_id,suppliers_name,contact,city)
values(102,"Office Supplies LTD","03111234567","Lahore");

insert into Suppliers
(suppliers_id,suppliers_name,contact,city)
values(103,"Furniture Hub","03221234567","Islamabad");

INSERT INTO Products
(product_id, product_name, category_id, suppliers_id, quantity, price)
VALUES
(1001,'HP Laptop',1,101,15,85000),
(1002,'Dell Monitor',1,101,20,32000),
(1003,'Logitech Mouse',1,101,50,2500),
(1004,'Mechanical Keyboard',1,101,25,5500),
(1005,'Notebook Pack',2,102,100,500),
(1006,'Ball Pen Box',2,102,80,300),
(1007,'Printer Paper',2,102,60,1200),
(1008,'Office Chair',3,103,8,15000),
(1009,'Study Table',3,103,5,25000),
(1010,'Bookshelf',3,103,3,18000);

INSERT INTO stock_transactions
(transaction_id, product_id, transaction_type, quantity, transaction_date)
VALUES
(1,1001,'IN',15,'2026-06-01'),
(2,1002,'IN',20,'2026-06-01'),
(3,1003,'IN',50,'2026-06-02'),
(4,1004,'IN',25,'2026-06-02'),
(5,1005,'IN',100,'2026-06-03'),
(6,1008,'IN',8,'2026-06-03'),
(7,1001,'OUT',2,'2026-06-05'),
(8,1003,'OUT',5,'2026-06-06'),
(9,1009,'IN',5,'2026-06-07'),
(10,1010,'IN',3,'2026-06-08');

select * from Categories;

select * from Suppliers;

select * from Products;

select * from stock_transactions;

select product_name,price,quantity from Products;

select * from Products
where price>10000;

select * from Products
where quantity<10;

select * from Products
order by price desc;

select * from Products
order by product_name asc;

select count(product_name) from Products;

select avg(price) from Products;

select max(price) from Products;

select min(price) from Products;

select sum(quantity) from Products;

select c.category_name,count(*)
from Products p
inner join Categories c
on p.category_id=c.category_id
group by c.category_name;

select c.category_name,avg(price)
from Products p
inner join Categories c
on p.category_id=c.category_id
group by c.category_name;

select c.category_name,sum(quantity)
from Products p
inner join Categories c
on p.category_id=c.category_id
group by c.category_name;

select s.suppliers_name,count(*)
from Products p
inner join Suppliers s
on p.suppliers_id=s.suppliers_id
group by s.suppliers_name;

select c.category_name,sum(quantity*price)
from Products p
inner join Categories c
on p.category_id=c.category_id
group by c.category_name;

select c.category_name,count(*)
from Products p
inner join Categories c
on p.category_id=c.category_id
group by c.category_name
having count(*)>2;

select s.suppliers_name,count(*)
from Products p
inner join Suppliers s
on p.suppliers_id=s.suppliers_id
group by s.suppliers_name
having count(*)>2;

select c.category_name,avg(price)
from Products p
inner join Categories c
on p.category_id=c.category_id
group by c.category_name
having avg(price)>10000;

select * from Products
where quantity<10;

select * from Products
where quantity=0;

select *
from Products
order by price desc
limit 1;

select *
from Products
order by price asc
limit 1;

select *
from Products
order by price desc
limit 5;

select sum(quantity*price)
from Products;

select p.product_name,transaction_type,stock_transactions.quantity,transaction_date
from stock_transactions
inner join Products p
on stock_transactions.product_id=p.product_id;

select category_name,
product_id,
product_name,
quantity,
price
from Categories
inner join Products
on Categories.category_id=Products.category_id;

select product_name,suppliers_name
from Products
inner join Suppliers
on Products.suppliers_id=Suppliers.suppliers_id;

select product_name,
category_name,
suppliers_name,
price
from Products
inner join Categories
on Products.category_id=Categories.category_id
inner join Suppliers
on Products.suppliers_id=Suppliers.suppliers_id;

SELECT USER();

create view low_stock_products as
select *
from Products
where quantity<10;

select * from low_stock_products;