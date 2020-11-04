-- Ecrire une requête afin de créer une table products qui permet de stocker les produits avec les informations suivantes:
-- serial_number est la colonne permettant de stocker l'id de chaque produit
-- label pour stocker son libellé
-- price_ht pour stocker son prix HT
-- price_ttc pour stocker son prix TTC
-- expiration_date pour stocker la date d'expiration du produit

-- Ajouter une table categories avec l'id de la catégorie et le libellé de la catégorie
-- Ajouter une clé étrangère à la table products afin de la relier à la table categories "prd_cat_category_id_fk"
-- Ajouter des contraintes afin de n'accepter que les prix > 0 et les dates d'expiration supérieures à la date d'aujourd'hui

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
        CONSTRAINT prd_label_uk UNIQUE (label),
        CONSTRAINT prd_cat_category_id_fk FOREIGN KEY (category_id)
            REFERENCES categories(category_id)
            ON DELETE SET NULL
            --ON DELETE CASCADE
    );
    
INSERT INTO products VALUES(1111, 'Imprimante', 100, 120, '12/12/2021', 10);
INSERT INTO products VALUES(1112, 'Laptop', 100, 120, '12/12/2021', 10);
INSERT INTO products VALUES(1113, 'Airpods', 100, 120, '12/12/2021', 20);
INSERT INTO products VALUES(1114, 'Micro', 100, 120, '12/12/2021', 20);
INSERT INTO products VALUES(1115, 'TV', 100, 120, '12/12/2021', 20);

COMMIT;

CREATE TABLE categories
    (
        category_id NUMBER(4) CONSTRAINT cat_category_id_pk PRIMARY KEY,
        label VARCHAR2(30)
    );

INSERT INTO categories VALUES(10,'Bureautique');
INSERT INTO categories VALUES(20,'Multimédia');

INSERT INTO categories VALUES(30,'Dummy');

DELETE 
FROM categories 
WHERE category_id = 20;

COMMIT;
    