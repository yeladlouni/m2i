-- S�lectionner les employ�s avec le nom du d�partement auquel ils sont affect�s

-- 1�re syntaxe (ambigu�t� en cas de pr�sence de deux colonnes en commun)

SELECT employee_id, first_name, last_name, department_name
FROM employees
NATURAL JOIN departments;

-- 2�me syntaxe

SELECT employee_id, first_name, last_name, department_name
FROM employees
JOIN departments USING (department_id);

-- 3�me syntaxe

SELECT employee_id, first_name, last_name, department_name
FROM employees
JOIN departments  ON employees.department_id = departments.department_id;


-- S�lectionner les employ�s m�me ceux qui ne sont affect�s � aucun d�partement

SELECT employee_id, first_name, last_name, emp.department_id, dpt.department_name
FROM employees emp
LEFT OUTER JOIN departments dpt ON emp.department_id = dpt.department_id;

-- S�lectionner les employ�s affect�s aux diff�rents d�partrments et afficher m�me les d�partements auquels aucun employ� n'est affect�

SELECT employee_id, first_name, last_name, department_name
FROM employees emp
RIGHT OUTER JOIN departments dpt ON emp.department_id = dpt.department_id


-- S�lectionner les employ�s affect�s aux diff�rents d�partements ainsi que les employ�s qui ne sont affect�s � aucun des d�partement
-- et les d�partement auquels aucun employ� n'est affect�

SELECT employee_id, first_name, last_name, department_name
FROM employees emp
FULL OUTER JOIN departments dpt ON emp.department_id = dpt.department_id


-- Exemple 1: Afficher pour les employ�s le ID, le pr�nom, le nom, le salaire et le nom du d�partement auquel il est affect�

SELECT employee_id, first_name, last_name, salary, department_name
FROM employees emp
LEFT OUTER JOIN DEPARTMENTS dpt ON (emp.department_id = dpt.department_id);

-- Exemple 2: Afficher pour les employ�s l'ID, le pr�nom, le nom, le salaire et le nom du d�partement auquel il est affect�
-- Pour les employ�s qui ne sont affect�s � aucun d�partement, afficher "Non affect�" comme nom de d�partement


SELECT employee_id, first_name, last_name, salary, NVL(department_name,'Non affect�')
FROM employees emp
LEFT OUTER JOIN DEPARTMENTS dpt ON (emp.department_id = dpt.department_id);

-- Ecrire une requ�te afin d'afficher pour chaque d�partement, le nom de d�partement et le nombre d'employ�s affect�s
SELECT department_name, COUNT(employee_id)
FROM employees
JOIN departments USING (department_id)
GROUP BY department_name;


-- Ecrire une requ�te afin d'afficher pour chaque d�partement, le nom de d�partement et le nombre d'employ�s affect�s
-- Afficher un nombre d'employ�s � 0 pour les d�partements auquels aucun employ� n'est affect�

SELECT NVL(department_name, 'Autres'), COUNT(employee_id)
FROM employees emp
LEFT OUTER JOIN departments dpt ON (emp.department_id = dpt.department_id)
GROUP BY department_name;

-- Ecrire une requ�te pour afficher le nom des d�partement auquels sont affect�s plus que 10 employ�s
SELECT NVL(department_name, 'Autres'), COUNT(employee_id)
FROM employees emp
LEFT OUTER JOIN departments dpt ON (emp.department_id = dpt.department_id)
GROUP BY department_name
HAVING COUNT(employee_id) > 10
ORDER BY COUNT(employee_id);



-- Ecrire une requ�te pour afficher le total des salaires par d�partement, afficher 0 pour les d�partements auquels aucun 
-- employ� n'est affect�


