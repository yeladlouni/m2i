-- UNION il permet de faire l'union de deux ou plusieurs tables

SELECT *
FROM employees
WHERE department_id IN (10, 20);

-- La requête équivalente en utilisant UNION

SELECT *
FROM employees
WHERE department_id = 10
UNION
SELECT *
FROM employees
WHERE department_id = 20;

-- Et si on avait plusieurs départements?

SELECT employee_id
FROM employees
WHERE department_id = 10
UNION
SELECT employee_id
FROM employees
WHERE department_id = 20
UNION
SELECT employee_id
FROM employees
WHERE department_id = 50;

-- Et si je veux afficher les départments qui ont des employés?

SELECT DISTINCT department_id
FROM employees;

-- Ou alors utiliser INTERSECT

SELECT department_id
FROM departments
INTERSECT
SELECT department_id
FROM employees;

-- A U B  = B U A  
-- A ^ B = B ^ A 
-- A - B <> B - A

-- UNION ALL permet de renvoyer l'ensemble des résultats y compris les doublons

-- MINUS  permet de renvoyer les enregistements qui sont sur la première table et pas ceux qui sont sur la deuxième table


-- Ecrire une requête en utilsiant MINUS afin de renvoyer l'id de l'employé ainsi que son nom complet pour les employés de la région d'amérique

SELECT *
FROM employees
WHERE department_id = 10
MINUS
SELECT *
FROM departments
WHERE manager_id IS NULL;
