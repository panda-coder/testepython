#!/bin/bash
#
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
CREATE TABLE marketplace_google (
id serial NOT NULL,
ean int8 NOT NULL,
"data" date NOT NULL,
        hora time NULL,
status bpchar(1) NOT NULL,                      
url text NULL,
imagem text NULL,
CONSTRAINT marketplace_google_ix1 UNIQUE (ean, data),
CONSTRAINT marketplace_google_pkey PRIMARY KEY (id, ean, data)
);

CREATE TABLE preco_marketplace_google (
id int4 NOT NULL,
preco float8 NULL,
parcela int4 NULL,
valor_parcela float8 NULL,
taxa_juros varchar(45) NULL,
vendedor varchar(255) NULL
);
EOSQL
