
CREATE VIEW employees_without_salary
AS
SELECT employee_id, department_id, first_name, last_name, manager_id
FROM hr.employees;


SELECT * FROM employees_without_salary

-- Accorder les droits à l'utilisateur shopping afin qu'il puisse accéder à la table employees

GRANT SELECT ON hr.employees to shopping;


-- Créer un utilisateur en utlisant une requête SQL

CREATE USER yassine2 IDENTIFIED BY yassine_2020;

-- Accorder le droit de connexion à l'utilisateur yassine2

GRANT CREATE SESSION TO yassine2;

-- Accorder le droit de création des tables à l'utilisateur yassine2

GRANT CREATE TABLE TO yassine2;

-- Accorder le droit de consulter les données, les modifier et les supprimer pour la table employees

GRANT SELECT, UPDATE, DELETE ON hr.employees TO yassine2;

-- Créer un rôle manager avec le droit de consulter, mettre à jour et supprimer les données de la table products

CREATE ROLE manager;  -- Créer le rôle manager

GRANT SELECT, UPDATE, DELETE ON shopping.products to manager; -- Accorder les droits de consultation, modification et suppression sur toutes les tables

GRANT manager TO yassine2; -- Accorde le rôle manager à l'utilisateur yassine2
 
CREATE ROLE marketing; -- Création du rôle marketing

GRANT SELECT ON products TO marketing; -- Accorder le droit de consultation de la table products au rôle marketing

CREATE USER dupont IDENTIFIED BY yassine_2020; -- Créer l'utilisateur dupont avec le mot de passe yassine_2020

GRANT marketing TO dupont; -- Accorder le rôle marketing à l'utilisateur dupont


GRANT UNLIMITED TABLESPACE TO yassine2; -- Donner le droit de création de données à yassine, Quota illimitée (espace disque)

ALTER USER yassine2 QUOTA 100M ON USERS; -- Spécifier un quota pour un utilisateur sur le tablespace USERS