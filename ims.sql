create database inventory;
use inventory;

create table supplier(
supplier_id int auto_increment,
supplier_name varchar(20),
supplier_phoneno numeric(10),
supplier_email varchar(30),
supplier_address varchar(30),
supplier_password varchar(8),
PRIMARY KEY(supplier_id)
);

insert into supplier (supplier_name, supplier_phoneno, supplier_email, supplier_address, supplier_password) values
('Supplier 1', '1234567890', 'supplier1@gmail.com', 'Address 1', '1111'),
('Supplier 2', '9876543210', 'supplier2@gmail.com', 'Address 2', '2222');

create table customer(
customer_id int auto_increment,
supplier_id int,
customer_name varchar(20),
customer_phoneno numeric(10),
customer_email varchar(30),
customer_address varchar(30),
PRIMARY KEY(customer_id),
FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
);

insert into customer (supplier_id, customer_name, customer_phoneno, customer_email, customer_address) values
('1', 'Customer 1', '1234567890', 'customer1@gmail.com', 'Address 1'),
('2', 'Customer 2', '9876543210', 'customer2@gmail.com', 'Address 2');

create table product(
item_id int auto_increment,
supplier_id int,
item_name varchar(20),
item_description varchar(30),
item_price decimal(10, 2),
item_quantity int,
PRIMARY KEY(item_id),
FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
);

insert into product (supplier_id, item_name, item_description, item_price, item_quantity) values
('1', 'Product 1', 'Description 1', '100.00', '10'),
('2', 'Product 2', 'Description 2', '200.00', '20');

create table order_(
order_id int auto_increment,
item_id int,
customer_id int,
supplier_id int,
order_date date,
order_quantity int,
total_price decimal(10, 2),
PRIMARY KEY(order_id),
FOREIGN KEY (item_id) REFERENCES product(item_id),
FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
);

insert into order_ (item_id, customer_id, supplier_id, order_date, order_quantity, total_price) values
('1', '1', '1', '2023-04-01', '5', '500.00'),
('1', '1', '1', '2023-04-01', '3', '300.00'),
('2', '2', '2', '2023-04-02', '2', '400.00'),
('2', '2', '2', '2023-04-02', '10', '2000.00');

create table payment(
item_id int,
order_id int,
customer_id int,
payment_date date,
payment_method varchar(20),
payment_amount decimal(10, 2),
FOREIGN KEY (item_id) REFERENCES product(item_id),
FOREIGN KEY (order_id) REFERENCES order_(order_id),
FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

insert into payment (item_id, order_id, customer_id, payment_date, payment_method, payment_amount) values
('1', '1', '1', '2023-04-01', 'Credit Card', '500.00'),
('1', '2', '1', '2023-04-01', 'UPI', '300.00'),
('2', '3', '2', '2023-04-02', 'UPI', '400.00'),
('2', '4', '2', '2023-04-02', 'Cash', '2000.00');

create table shipment(
item_id int,
order_id int,
customer_id int,
shipment_date date,
shipment_status varchar(20),
FOREIGN KEY (item_id) REFERENCES product(item_id),
FOREIGN KEY (order_id) REFERENCES order_(order_id),
FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

insert into shipment (item_id, order_id, customer_id, shipment_date, shipment_status) values 
('1', '1', '1', '2023-04-01', 'Shipped'),
('1', '2', '1', '2023-04-01', 'Shipped'),
('2', '3', '2', '2023-04-02', 'Ready to Ship'),
('2', '4', '2', '2023-04-02', 'Delivered');

create table invoice(
item_id int,
order_id int,
customer_id int,
invoice_date date,
total_amount decimal(10, 2),
FOREIGN KEY (item_id) REFERENCES product(item_id),
FOREIGN KEY (order_id) REFERENCES order_(order_id),
FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

insert into invoice (item_id, order_id, customer_id, invoice_date, total_amount) values 
('1', '1', '1', '2023-04-01', '500.00'),
('1', '2', '1', '2023-04-01', '300.00'),
('2', '3', '2', '2023-04-02', '400.00'),
('2', '4', '2', '2023-04-02', '2000.00');


-- drop database inventory;