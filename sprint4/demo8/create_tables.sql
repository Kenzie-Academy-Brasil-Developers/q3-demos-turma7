DROP TABLE IF EXISTS users, orders, invoices, products, orders_products;

-- table users
CREATE TABLE IF NOT EXISTS users (
    user_id       	SERIAL PRIMARY KEY,
    email           VARCHAR(64) UNIQUE NOT NULL,
    birthdate       DATE NOT NULL,
    children        INT NOT NULL,
    married         BOOLEAN NOT NULL,
    account_balance REAL NOT NULL
);

-- table orders
CREATE TABLE IF NOT EXISTS orders (
    order_id        SERIAL PRIMARY KEY,
    order_date      TIMESTAMP NOT NULL,
    customer_id     INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES users("user_id")
    -- customer_id INT NOT NULL REFERENCES users("user_id")
    -- FOREIGN KEY (customer_id) REFERENCES users(user_id) ON DELETE CASCADE;
);

-- table invoices
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id 		SERIAL PRIMARY KEY,
    release_date 	DATE NOT NULL,
    invoice_number 	VARCHAR(64) UNIQUE,
    order_id 		INT UNIQUE NOT NULL REFERENCES orders("order_id")
);

-- table products
CREATE TABLE IF NOT EXISTS products(
	product_id 		SERIAL 		PRIMARY KEY,
	"name" 			VARCHAR(50) NOT NULL,
	price 			REAL 		NOT NULL
);


-- table orders_products
CREATE TABLE IF NOT EXISTS orders_products(
	orders_products_id 	SERIAL 	PRIMARY KEY,
	sale_value 			REAL,
	order_id 			INTEGER NOT NULL,
	product_id 			INTEGER NOT NULL,
	FOREIGN KEY (order_id) 		REFERENCES orders("order_id"),
	FOREIGN KEY (product_id) 	REFERENCES products("product_id")
);