CREATE TABLE IF NOT EXISTS estados(
	id 			BIGSERIAL 	PRIMARY KEY,
	nome		VARCHAR(30) NOT NULL UNIQUE,
	sigla		VARCHAR(2)	NOT NULL UNIQUE,
	capital 	VARCHAR(30) NOT NULL UNIQUE,
	regiao		VARCHAR(30),
	populacao 	DECIMAL,
	"area" 		DECIMAL
);

INSERT INTO estados
	(nome, sigla, capital, populacao, "area", regiao)
VALUES
	('Santa Catarina', 'SC', 'Florianópolis', 7, 95.1, 'Sul'),
	('Rio Grande do Sul', 'RS', 'Porto Alegre', 11, 281, 'Sul'),
	('São Paulo', 'SP', 'São Paulo', 44, 248.2, 'Sudeste'),
	('Rio de Janeiro', 'RJ', 'Rio de Janeiro', 16, 43.6, 'Sudeste'),
	('Minas Gerais', 'MG', 'Belo Horizonte', 20.8, NULL, 'Sudeste'),
	('Bahia', 'BA', 'Salvador', 15, 567.2, 'Nordeste'),
	('Maranhão', 'MA', 'Sao Luis', 6.8, 331, 'Nordeste'),
	('Espirito Santo', 'ES', 'Vitória', NULL, 20.9, 'Sudeste');

SELECT * FROM estados;

-- Registros que tenham como segunda letra 'a'
SELECT
	id, nome, capital
FROM
	estados e
WHERE nome
	LIKE '_a%';


-- Operador de diferença
SELECT
	id, nome, capital
FROM
	estados e
WHERE nome
	LIKE capital
	AND id % 2 <> 0;

-- Ordenamento
SELECT * FROM estados ORDER BY sigla;

SELECT * FROM estados ORDER BY sigla DESC;

SELECT * FROM estados ORDER BY regiao DESC, populacao DESC;

-- Limitando a busca
SELECT * FROM estados ORDER BY regiao, populacao LIMIT 2;

SELECT * FROM estados LIMIT 2;

SELECT * FROM estados;

-- Limitando a busca começando pelo registro 3
SELECT * FROM estados LIMIT 2 OFFSET 3;

-- Agrupamento
SELECT regiao, COUNT(*) FROM estados GROUP BY regiao;

SELECT regiao, SUM(e."area") FROM estados e GROUP BY regiao;

-- Errado
SELECT
	regiao, SUM(e."area")
FROM estados e
GROUP BY regiao
WHERE SUM(e."area") > 350;

-- Certo
SELECT
	regiao, SUM(e."area")
FROM estados e
GROUP BY regiao
	HAVING SUM(e."area") > 350;

-- Aninhando filtros
SELECT
	regiao, SUM(e."area")
FROM estados e
GROUP BY regiao
	HAVING SUM(e."area") > 350
ORDER BY SUM(e."area") LIMIT 1 OFFSET 1;


-- Update com returning
UPDATE
	estados e
SET
	populacao = 3.9
WHERE sigla = 'ES'
RETURNING *;

-- Update de multiplos registros
UPDATE
	estados e
SET
	"area" = 586
WHERE "area" IS NULL
RETURNING *;


-- Modificando caracteristicas primarias das colunas da tabela
ALTER TABLE
	estados
ADD COLUMN
	clinma VARCHAR(50);

ALTER TABLE
	estados
RENAME clinma TO clima;

ALTER TABLE estados DROP COLUMN IF EXISTS clima;

/*
 * Processo de criação da coluna e update do valor dela para um DEFAULT
 * Processo bem gastoso em recursos.
 */
ALTER TABLE
	estados
ADD COLUMN
	clima VARCHAR(50) DEFAULT 'tropical';

ALTER TABLE
	estados
ALTER COLUMN
	populacao
SET NOT NULL;

SELECT * FROM estados;

/*
 * Alterando tipo de uma coluna e convertendo dados
 * ja existentes para inteiro
 */
ALTER TABLE
	estados
ALTER COLUMN
	populacao
TYPE INTEGER
	USING populacao::INTEGER;


INSERT INTO
	estados (nome, sigla, capital, populacao, "area", "regiao")
VALUES
	('Goiás', 'GO', 'Goiânia', 6, 340, 'Centro Oeste')
RETURNING *;

DELETE FROM
	estados
WHERE id = 9
RETURNING *;

INSERT INTO
	estados (nome, sigla, capital, populacao, "area", "regiao")
VALUES
	('Goiás', 'GO', 'Goiânia', 6, 340, 'Centro Oeste')
RETURNING *;


SELECT * FROM estados;

DELETE FROM
	estados
WHERE
	sigla LIKE 'GO'
	OR populacao < 5
RETURNING *;
