/*
	31/01
*/
-- 1:N
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


-- Sub query
SELECT
	*
FROM
	users u
JOIN
	orders o
	ON u.user_id = o.customer_id
WHERE
	u.user_id = (SELECT user_id FROM users WHERE email LIKE 'carlos@email.com');

/*
	01/02
*/

-- DELETE em tabelas que se relacionam
DELETE FROM users WHERE user_id = 3;


ALTER TABLE
	orders
DROP CONSTRAINT
	"orders_customer_id_fkey";

ALTER TABLE
	orders
ADD CONSTRAINT
	"orders_users_fk"
FOREIGN KEY (customer_id) REFERENCES users(user_id) ON DELETE CASCADE;

-- MUITO CUIDADO COM DELETE CASCADE
DELETE FROM users WHERE user_id = 3;

-- Quebra regra de UNIQUE da FK em invoices
INSERT INTO invoices
    (release_date, invoice_number, order_id)
VALUES
    ('2021-11-08 05:39:15', '32752374698326546572341', 1);

-- Selects 1:1
SELECT * FROM invoices;

SELECT
	*
FROM
	invoices i
JOIN
	orders o
	ON i.order_id = o.order_id;

SELECT
	*
FROM
	invoices i
JOIN
	orders o
	ON i.order_id = o.order_id
WHERE
	o.order_id = 3;

SELECT
	*
FROM
	invoices i
JOIN
	orders o
	ON i.order_id = o.order_id
JOIN
	users u
	ON u.user_id = o.customer_id
WHERE
	u.user_id = 3;

SELECT
	u.user_id, u.email, i.*
FROM
	invoices i
JOIN
	orders o
	ON i.order_id = o.order_id
JOIN
	users u
	ON u.user_id = o.customer_id
WHERE
	u.user_id = 3;