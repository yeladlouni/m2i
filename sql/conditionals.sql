SELECT employee_id, first_name, last_name, department_id,
CASE department_id
WHEN 50 THEN 'Logistiques'
WHEN 80 THEN 'Commercial'
ELSE 'Autres'
END department
FROM employees;


-- Ecrire une requête en utilisant CASE afin d'afficher 'inf' pour les employés affectés à un départment dont l'ID est <= 50
-- 'mid' pour les employés qui sont affectés à un déapartement >50 et <= 80 et 'sup' pour ceux qui ont un département id > 80

SELECT employee_id, first_name, last_name, department_id,
CASE 
    WHEN department_id <=50 THEN 'inf'
    WHEN department_id > 50 AND department_id <= 80 THEN 'mid'
    ELSE 'sup'
END department
FROM employees;

-- Création de vue/view à partir de la requête précédente

CREATE VIEW my_departments
AS
SELECT employee_id, first_name, last_name, department_id,
CASE 
    WHEN department_id <=50 THEN 'inf'
    WHEN department_id > 50 AND department_id <= 80 THEN 'mid'
    ELSE 'sup'
END department
FROM employees;

SELECT * FROM my_departments;
