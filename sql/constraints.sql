-- Ecrire une requête afin de créer une table products qui permet de stocker les produits avec les informations suivantes:
-- serial_number est la colonne permettant de stocker l'id de chaque produit
-- label pour stocker son libellé
-- price_ht pour stocker son prix HT
-- price_ttc pour stocker son prix TTC
-- expiration_date pour stocker la date d'expiration du produit

-- Ajouter une table categories avec l'id de la catégorie et le libellé de la catégorie
-- Ajouter une clé étrangère à la table products afin de la relier à la table categories "prd_cat_category_id_fk"

DROP TABLE products;

CREATE TABLE products
    (
        serial_number NUMBER(6),
        label VARCHAR2(30),
        price_ht NUMBER(6,2),
        price_ttc NUMBER(6,2),
        expiration_date DATE,
        category_id NUMBER(4),
        CONSTRAINT prd_serial_number_pk PRIMARY KEY (serial_number),  -- nom mnémonique  facile à retenir
        CONSTRAINT prd_label_uk UNIQUE (label)
    );
    
    
CREATE TABLE categories
    (
        category_id NUMBER(4) CONSTRAINT cat_category_id_pk PRIMARY KEY,
        label VARCHAR2(30)
    );


    
    