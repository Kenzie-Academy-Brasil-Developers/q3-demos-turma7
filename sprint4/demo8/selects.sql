SELECT
	o.*, p.*
FROM orders o
JOIN
	orders_products op
	ON o.order_id = op.order_id
JOIN
	products p
	ON p.product_id = op.product_id
WHERE
	o.order_id = 3;


SELECT
	o.order_id, p."name", p.price, op.sale_value
FROM orders o
JOIN
	orders_products op
	ON o.order_id = op.order_id
JOIN
	products p
	ON p.product_id = op.product_id
WHERE
	o.order_id = 3;

SELECT
	p."name", op.sale_value
FROM orders o
JOIN
	orders_products op
	ON o.order_id = op.order_id
JOIN
	products p
	ON p.product_id = op.product_id
WHERE
	o.order_id = 3;

SELECT
	u.user_id, u.email,
	o.order_id, o.order_date,
	i.invoice_number, i.release_date
FROM
	invoices i
JOIN
	orders o
	ON i.order_id = o.order_id
JOIN
	users u
	ON o.customer_id = u.user_id
WHERE
	u.user_id =3;


-- Between
SELECT
	*
FROM
	users u
WHERE
	account_balance >= 7500
	AND account_balance <= 10000;

SELECT
	*
FROM
	users u
WHERE
	account_balance BETWEEN 7500 AND 10000;

-- IN
SELECT
	*
FROM
	users
WHERE
	children = 3 OR children = 1;

SELECT
	*
FROM
	users
WHERE
	children IN (1, 2);


-- Subquery
SELECT
	*
FROM
	users
WHERE
	children IN (0, 3);

SELECT
	*
FROM
	users
WHERE
	children IN (
			(SELECT min(children) FROM users),
			(SELECT max(children) FROM users)
);

INSERT INTO users
    (email, birthdate, children, married, account_balance)
VALUES
	('aaaaaaaaaa@email.com', '1995-12-27', 10, TRUE, 7500);


SELECT avg(account_balance) FROM users;

SELECT
	user_id, email, account_balance
FROM
	users
WHERE
	account_balance > (SELECT avg(account_balance) FROM users);

-- date process
SELECT * FROM invoices;

SELECT current_date;

SELECT date_part('month', CURRENT_DATE);
SELECT date_part('year', CURRENT_DATE);
SELECT date_part('century', CURRENT_DATE);

SELECT to_char(current_date, 'YYYY-MM');

SELECT
	*
FROM
	invoices
WHERE
	to_char(release_date , 'YYYY-MM') = (SELECT to_char(current_date, 'YYYY-MM'))

-- Select INTO
SELECT
	*
INTO
	logs
FROM
	invoices
WHERE
	to_char(release_date , 'YYYY-MM') = (SELECT to_char(current_date, 'YYYY-MM'));

SELECT
	u.email, i.invoice_number, i.release_date
INTO
	logs
FROM
	invoices i
JOIN
	orders o
	ON i.order_id = o.order_id
JOIN
	users u
	ON u.user_id = o.customer_id
WHERE
	to_char(i.release_date , 'YYYY-MM') = (SELECT to_char(current_date, 'YYYY-MM'));