
CREATE VIEW employees_without_salary
AS
SELECT employee_id, department_id, first_name, last_name, manager_id
FROM hr.employees;


SELECT * FROM employees_without_salary

-- Accorder les droits � l'utilisateur shopping afin qu'il puisse acc�der � la table employees

GRANT SELECT ON hr.employees to shopping;


-- Cr�er un utilisateur en utlisant une requ�te SQL

CREATE USER yassine2 IDENTIFIED BY yassine_2020;

-- Accorder le droit de connexion � l'utilisateur yassine2

GRANT CREATE SESSION TO yassine2;

-- Accorder le droit de cr�ation des tables � l'utilisateur yassine2

GRANT CREATE TABLE TO yassine2;

-- Accorder le droit de consulter les donn�es, les modifier et les supprimer pour la table employees

GRANT SELECT, UPDATE, DELETE ON hr.employees TO yassine2;

-- Cr�er un ro