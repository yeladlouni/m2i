-- Les fonctions d'aggrÃ©gation

-- La masse salariale

SELECT SUM(salary)
FROM employees;

-- Le nombre d'employÃ©s

SELECT SUM(commission_pct)
FROM employees;

SELECT COUNT(employee_id)
FROM employees;

-- Pour plus de performance, on utilise COUNT(1)
SELECT COUNT(1)
FROM employees;

-- La valeur maximale des salaires

SELECT MIN(salary), MAX(salary), ROUND(AVG(salary), 2)
FROM employees;


SELECT COUNT(1), MIN(salary), MAX(salary), AVG(salary), VARIANCE(salary), STDDEV(salary)
FROM employees
WHERE job_id LIKE '%REP%';

-- Le nombre des prénoms des employés avec les doublons

SELECT COUNT(first_name)
FROM employees;


-- Afficher le comptes des prénoms distincts d'employés

SELECT COUNT(DISTINCT first_name)
FROM employees;

-- La fonction AVG pour une colonne qui contient des null, le COUNT est différent pour les deux requêtes 

SELECT AVG(commission_pct)
FROM employees;

SELECT AVG(NVL(commission_pct, 0))
FROM employees;

-- Afficher le salaire total par département

SELECT department_id, SUM(salary)
FROM employees
GROUP BY department_id

-- Ecrire une requête qui permet d'afficher le salaire total par département et par fonction

SELECT department_id, SUM(salary) "Somme des salaires", COUNT(employee_id)
FROM employees
WHERE job_id LIKE '%REP%'
GROUP BY department_id
HAVING COUNT(employee_id) = 1;