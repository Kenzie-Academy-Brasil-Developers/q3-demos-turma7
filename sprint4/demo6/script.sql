CREATE TABLE IF NOT EXISTS users (
    "user_id"       SERIAL PRIMARY KEY,
    email           VARCHAR(64) UNIQUE NOT NULL,
    birthdate       DATE NOT NULL,
    children        INT NOT NULL,
    married         BOOLEAN NOT NULL,
    account_balance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    order_id        SERIAL PRIMARY KEY,
    order_date      TIMESTAMP NOT NULL,
    customer_id     INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES users("user_id")
);

-- customer_id INT NOT NULL REFERENCES users("user_id")

INSERT INTO users
    (email, birthdate, children, married, account_balance)
VALUES
	('roberto@email.com', '1995-12-27', 3, TRUE, 7500),
    ('maria@email.com', '1990-06-14', 0, FALSE, 15000),
    ('carlos@email.com', '1980-12-11', 2, TRUE, 10000),
    ('joao@email.com', '2003-11-18', 0, FALSE, 0),
    ('renata@email.com', '1999-01-04', 0, FALSE, 18000),
    ('wesley@email.com', '2007-06-06', 0, FALSE, 15),
    ('ana@email.com', '1979-10-11', 2, TRUE, 80000),
    ('ricardo@email.com', '1989-12-13', 2, TRUE, 20000);

SELECT * FROM users;

INSERT INTO
	orders (customer_id, order_date)
VALUES
	(1, '2021-11-08 05:28:15'), -- ORDER associada ao USER de id 1
    (2, '2021-11-13 03:53:54'), -- ORDER associada ao USER de id 2
	(3, '2021-11-16 12:55:35'), -- ORDER associada ao USER de id 3
	(3, '2021-11-20 20:02:13'); -- ORDER associada ao USER de id 3

SELECT * FROM orders;

SELECT
	*
FROM
	users u
JOIN
	orders o
	ON u.user_id = o.customer_id;

SELECT
	*
FROM
	users u
JOIN
	orders o
	ON u.user_id = o.customer_id
WHERE
	u.user_id = 3;

SELECT
	u.married, COUNT(*)
FROM
	users u
JOIN
	orders o
	ON u.user_id = o.customer_id
GROUP BY
	u.married;


-- Sub querys
SELECT
	*
FROM
	users u
JOIN
	orders o
	ON u.user_id = o.customer_id
WHERE
	u.user_id = (SELECT user_id FROM users WHERE email LIKE 'carlos@email.com');

