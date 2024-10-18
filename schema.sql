USE wallet;

DROP TABLE IF EXISTS wallet.transactions;
DROP TABLE IF EXISTS wallet.accounts;
DROP TABLE IF EXISTS wallet.clients;
DROP TABLE IF EXISTS wallet.balances;

CREATE TABLE wallet.clients (id varchar(255), name varchar(255), email varchar(255), created_at date);
CREATE TABLE wallet.accounts (id varchar(255), client_id varchar(255), balance int, created_at date);
CREATE TABLE wallet.transactions (id varchar(255), account_id_from varchar(255), account_id_to varchar(255), amount int, created_at date);
CREATE TABLE wallet.balances (account_id varchar(255), balance int, created_at date, updated_at date);

INSERT INTO wallet.clients (id, name, email, created_at) VALUES ('c3614322-208a-4c0c-8e1b-348306341ccd', 'John Doe', 'john@j.com', '2024-07-18');
INSERT INTO wallet.clients (id, name, email, created_at) VALUES ('a83e526f-a0f1-49a9-9d11-1783e53a31d7', 'Jane Doe', 'jane@j.com', '2024-07-18');

INSERT INTO wallet.accounts (id, client_id, balance, created_at) VALUES ('7154fdcc-731b-4564-ae5f-e3da98641be5', 'c3614322-208a-4c0c-8e1b-348306341ccd', 1000, '2024-07-18');
INSERT INTO wallet.accounts (id, client_id, balance, created_at) VALUES ('3428feff-f08f-4c09-8bc0-6c31dd10144a', 'a83e526f-a0f1-49a9-9d11-1783e53a31d7', 500, '2024-07-18');

INSERT INTO wallet.balances (account_id, balance, created_at) VALUES ('7154fdcc-731b-4564-ae5f-e3da98641be5', 1000, '2024-07-18');
INSERT INTO wallet.balances (account_id, balance, created_at) VALUES ('3428feff-f08f-4c09-8bc0-6c31dd10144a', 500, '2024-07-18');
