SELECT * FROM tabela_teste tt;

-- Comentario
DROP TABLE tabela_teste;


CREATE TABLE users();
CREATE TABLE IF NOT EXISTS users();

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
	id 			BIGSERIAL 	PRIMARY KEY,
	"name" 		VARCHAR(50) NOT NULL UNIQUE,
	birth_date 	DATE 		NOT NULL,
	created_at 	TIMESTAMPTZ DEFAULT NOW(),
	heigth 		DECIMAL,
	"quarter" 	VARCHAR(2)
);

SELECT NOW();

INSERT INTO
	users ("name", birth_date, heigth, "quarter")
VALUES
	('Chrystian', '1993-03-03', 1.78, 'Q3'),
	('Aroldo', '1982-10-23', 1.59, 'Q0'),
	('Joana', '1995-03-17', 1.80, 'M3');


SELECT * FROM users;

SELECT "name", "quarter" FROM users;


SELECT * FROM users WHERE heigth > 1.60;

SELECT *
FROM users
WHERE heigth > 1.60
	AND "quarter" LIKE 'Q3';

SELECT *
FROM users
WHERE heigth > 1.60
	AND "quarter" LIKE '%3';

-- Começa com 'Q'
SELECT *
FROM users
WHERE "quarter" LIKE 'Q%';

-- Tem 'A' em qualquer parte da string
SELECT *
FROM users
WHERE "name" LIKE '%A%';

-- Tem 'A' em qualquer parte da string e ignora case-sensitive
SELECT *
FROM users
WHERE "name" iLIKE '%A%';

-- Dando um apelido a coluna no select
SELECT "name" user_name FROM users;

-- Criando uma coluna extra de consulta (somente no select)
SELECT "name", age(birth_date) FROM users;

UPDATE users SET "quarter" = 'Q1' WHERE "name" LIKE 'Aroldo';

SELECT * FROM users;


DELETE FROM users WHERE "name" LIKE 'Aroldo';

SELECT * FROM users;

