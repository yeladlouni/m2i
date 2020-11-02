-- Sï¿½lectionner les employï¿½s avec le nom du dï¿½partement auquel ils sont affectï¿½s

-- 1ï¿½re syntaxe (ambiguï¿½tï¿½ en cas de prï¿½sence de deux colonnes en commun)

SELECT employee_id, first_name, last_name, department_name
FROM employees
NATURAL JOIN departments;

-- 2ï¿½me syntaxe

SELECT employee_id, first_name, last_name, department_name
FROM employees
JOIN departments USING (department_id);

-- 3ï¿½me syntaxe

SELECT employee_id, first_name, last_name, department_name
FROM employees
JOIN departments  ON employees.department_id = departments.department_id;


-- Sï¿½lectionner les employï¿½s mï¿½me ceux qui ne sont affectï¿½s ï¿½ aucun dï¿½partement

SELECT employee_id, first_name, last_name, emp.department_id, dpt.department_name
FROM employees emp
LEFT OUTER JOIN departments dpt ON emp.department_id = dpt.department_id;

-- Sï¿½lectionner les employï¿½s affectï¿½s aux diffï¿½rents dï¿½partrments et afficher mï¿½me les dï¿½partements auquels aucun employï¿½ n'est affectï¿½

SELECT employee_id, first_name, last_name, department_name
FROM employees emp
RIGHT OUTER JOIN departments dpt ON emp.department_id = dpt.department_id


-- Sï¿½lectionner les employï¿½s affectï¿½s aux diffï¿½rents dï¿½partements ainsi que les employï¿½s qui ne sont affectï¿½s ï¿½ aucun des dï¿½partement
-- et les dï¿½partement auquels aucun employï¿½ n'est affectï¿½

SELECT employee_id, first_name, last_name, department_name
FROM employees emp
FULL OUTER JOIN departments dpt ON emp.department_id = dpt.department_id


-- Exemple 1: Afficher pour les employï¿½s le ID, le prï¿½nom, le nom, le salaire et le nom du dï¿½partement auquel il est affectï¿½

SELECT employee_id, first_name, last_name, salary, department_name
FROM employees emp
LEFT OUTER JOIN DEPARTMENTS dpt ON (emp.department_id = dpt.department_id);

-- Exemple 2: Afficher pour les employï¿½s l'ID, le prï¿½nom, le nom, le salaire et le nom du dï¿½partement auquel il est affectï¿½
-- Pour les employï¿½s qui ne sont affectï¿½s ï¿½ aucun dï¿½partement, afficher "Non affectï¿½" comme nom de dï¿½partement


SELECT employee_id, first_name, last_name, salary, NVL(department_name,'Non affectï¿½')
FROM employees emp
LEFT OUTER JOIN DEPARTMENTS dpt ON (emp.department_id = dpt.department_id);

-- Ecrire une requï¿½te afin d'afficher pour chaque dï¿½partement, le nom de dï¿½partement et le nombre d'employï¿½s affectï¿½s
SELECT department_name, COUNT(employee_id)
FROM employees
JOIN departments USING (department_id)
GROUP BY department_name;


-- Ecrire une requï¿½te afin d'afficher pour chaque dï¿½partement, le nom de dï¿½partement et le nombre d'employï¿½s affectï¿½s
-- Afficher un nombre d'employï¿½s ï¿½ 0 pour les dï¿½partements auquels aucun employï¿½ n'est affectï¿½

SELECT NVL(department_name, 'Autres'), COUNT(employee_id)
FROM employees emp
LEFT OUTER JOIN departments dpt ON (emp.department_id = dpt.department_id)
GROUP BY department_name;

-- Ecrire une requï¿½te pour afficher le nom des dï¿½partement auquels sont affectï¿½s plus que 10 employï¿½s
SELECT NVL(department_name, 'Autres'), COUNT(employee_id)
FROM employees emp
LEFT OUTER JOIN departments dpt ON (emp.department_id = dpt.department_id)
GROUP BY department_name
HAVING COUNT(employee_id) > 10
ORDER BY COUNT(employee_id);



-- Ecrire une requï¿½te pour afficher le total des salaires par dï¿½partement, afficher 0 pour les dï¿½partements auquels aucun 
-- employï¿½ n'est affectï¿½

-- Une autre manière d'écrire les jointures

SELECT emp1.first_name, emp2.first_name
FROM employees emp1, employees emp2
WHERE emp1.employee_id = emp2.manager_id

-- Ecrire une requête afin d'afficher pour chaque nom de région, le nombre total des employés
-- Afficher 0 pour les régions sans employés