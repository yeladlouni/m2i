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
values ('209',NULL,'Dupont','dupont@gmail.com',NULL,SYSDATE,'SA_REP',NULL,NULL,NULL,50);

