-- Sélectionner les employés avec le nom du département auquel ils sont affectés

-- 1ère syntaxe (ambiguïté en cas de présence de deux colonnes en commun)

SELECT employee_id, first_name, last_name, department_name
FROM employees
NATURAL JOIN departments;

-- 2ème syntaxe

SELECT employee_id, first_name, last_name, department_name
FROM employees
JOIN departments USING (department_id);

-- 3ème syntaxe

SELECT employee_id, first_name, last_name, department_name
FROM employees
JOIN departments  ON employees.department_id = departments.department_id;


-- Sélectionner les employés même ceux qui ne sont affectés à aucun département

SELECT employee_id, first_name, last_name, emp.department_id, dpt.department_name
FROM employees emp
LEFT OUTER JOIN departments dpt ON emp.department_id = dpt.department_id;

-- Sélectionner les employés affectés aux différents départrments et afficher même les départements auquels aucun employé n'est affecté

SELECT employee_id, first_name, last_name, department_name
FROM employees emp
RIGHT OUTER JOIN departments dpt ON emp.department_id = dpt.department_id


-- Sélectionner les employés affectés aux différents départements ainsi que les employés qui ne sont affectés à aucun des département
-- et les département auquels aucun employé n'est affecté

SELECT employee_id, first_name, last_name, department_name
FROM employees emp
FULL OUTER JOIN departments dpt ON emp.department_id = dpt.department_id


-- Exemple 1: Afficher pour les employés le ID, le prénom, le nom, le salaire et le nom du département auquel il est affecté

SELECT employee_id, first_name, last_name, salary, department_name
FROM employees emp
LEFT OUTER JOIN DEPARTMENTS dpt ON (emp.department_id = dpt.department_id);

-- Exemple 2: Afficher pour les employés l'ID, le prénom, le nom, le salaire et le nom du département auquel il est affecté
-- Pour les employés qui ne sont affectés à aucun département, afficher "Non affecté" comme nom de département


SELECT employee_id, first_name, last_name, salary, NVL(department_name,'Non affecté')
FROM employees emp
LEFT OUTER JOIN DEPARTMENTS dpt ON (emp.department_id = dpt.department_id);

-- Ecrire une requête afin d'afficher pour chaque département, le nom de département et le nombre d'employés affectés
SELECT department_name, COUNT(employee_id)
FROM employees
JOIN departments USING (department_id)
GROUP BY department_name;


-- Ecrire une requête afin d'afficher pour chaque département, le nom de département et le nombre d'employés affectés
-- Afficher un nombre d'employés à 0 pour les départements auquels aucun employé n'est affecté

SELECT NVL(department_name, 'Autres'), COUNT(employee_id)
FROM employees emp
LEFT OUTER JOIN departments dpt ON (emp.department_id = dpt.department_id)
GROUP BY department_name;

-- Ecrire une requête pour afficher le nom des département auquels sont affectés plus que 10 employés
SELECT NVL(department_name, 'Autres'), COUNT(employee_id)
FROM employees emp
LEFT OUTER JOIN departments dpt ON (emp.department_id = dpt.department_id)
GROUP BY department_name
HAVING COUNT(employee_id) > 10
ORDER BY COUNT(employee_id);



-- Ecrire une requête pour afficher le total des salaires par département, afficher 0 pour les départements auquels aucun 
-- employé n'est affecté



-- Rappel: Le total des salaires est de 691416
