-- Describe permet de décrire une table 

DESCRIBE employees;

DESC employees;


-- Insérer des enregistrements dans une table

-- Insérer un nouveau département 999 qui a le nom dummy et dont la localistation est à Genève

DESC departments;

INSERT INTO departments(department_id,department_name, location_id) 
VALUES (999,'dummy',2900);

INSERT INTO departments  
VALUES (988,'dummy',NULL,2900);

COMMIT;  -- Permet de valider les changements

ROLLBACK; -- Permet d'annuler les changements

-- Aujourd'hui on vient de recruter un employé qui s'appelle Dupont mais on connait pas son nom encore
-- dans le département Shipping et qui n'a pas de manager pour le moment

-- Ecrire une requête afin de le stocker dans la base de données

INSERT INTO employees (EMPLOYEE_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,HIRE_DATE,JOB_ID,SALARY,COMMISSION_PCT,MANAGER_ID,DEPARTMENT_ID)
VALUES ('209',NULL,'Dupont','dupont@gmail.com',NULL,SYSDATE,'SA_REP',NULL,NULL,NULL,50);

COMMIT;

-- Création d'une table à partir d'un SELECT

CREATE TABLE department50
AS
SELECT *
FROM employees
WHERE department_id = 50;

-- Insérer dans la nouvelle table les employés du département 90

INSERT INTO department50
SELECT *
FROM employees
WHERE department_id = 90;

-- L'employé Dupont a changé son adresse email, la nouvelle est dupont_dupont@outlook.com
-- Ecrire une requête afin de mettre à jour son email

UPDATE employees
SET email = 'dupont_dupont@outlook.com'
WHERE LOWER(last_name) = 'dupont';

COMMIT;


-- On se trompe lors d'une instruction DELETE, on met pas de condition

DELETE FROM department50;

COMMIT;

ROLLBACK;  -- Si le commit a été déjà exécuté, on ne peut plus récupérer les données

-- DROP permet de supprimer une table ou un objet d'une manière générale

DROP TABLE department50;


-- SAVEPOINT permet de subdiviser le script en groupes

UPDATE departments
SET department_name = 'Logistiques'
WHERE department_name = 'Shipping';

SAVEPOINT A;

INSERT INTO departments
VALUES(777, 'Fraude interne', NULL, NULL);


DELETE FROM departments
WHERE department_id = 999;

SAVEPOINT B;

COMMIT TO A;

ROLLBACK TO B;

-- Pour les DDL = data definition language, elles permettent de créer, supprimer des objets/tables, e.g DROP, CREATE...
-- La même chose pour les DCL: data control language ==> gestion de permissions

-- Ecrire une requête afin de 
-- Créer une table employees_usa qui contient juste les employés qui sont situés aux USA
-- Ajouter un employé dummy à la table avec des données fictives en mettant comme date de recrutement 01/05/2020 et comme email test@gmail.com
-- Mettre à jour l'email de l'employé afin de le mettre en majuscules
-- Supprimer cet employé
-- Valider jusqu'à la MAJ afin que l'employé ne soit pas supprimé
