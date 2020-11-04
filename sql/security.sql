
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

-- Cr�er un r�le manager avec le droit de consulter, mettre � jour et supprimer les donn�es de la table products

CREATE ROLE manager;  -- Cr�er le r�le manager

GRANT SELECT, UPDATE, DELETE ON shopping.products to manager; -- Accorder les droits de consultation, modification et suppression sur toutes les tables

GRANT manager TO yassine2; -- Accorde le r�le manager � l'utilisateur yassine2
 
CREATE ROLE marketing; -- Cr�ation du r�le marketing

GRANT SELECT ON products TO marketing; -- Accorder le droit de consultation de la table products au r�le marketing

CREATE USER dupont IDENTIFIED BY yassine_2020; -- Cr�er l'utilisateur dupont avec le mot de passe yassine_2020

GRANT marketing TO dupont; -- Accorder le r�le marketing � l'utilisateur dupont


GRANT UNLIMITED TABLESPACE TO yassine2; -- Donner le droit de cr�ation de donn�es � yassine, Quota illimit�e (espace disque)

ALTER USER yassine2 QUOTA 100M ON USERS; -- Sp�cifier un quota pour un utilisateur sur le tablespace USERS