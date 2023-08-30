CREATE DATABASE pet_pals;

CREATE USER pet_pals_admin WITH PASSWORD 'petpalsadminpass';

GRANT ALL PRIVILEGES ON DATABASE pet_pals TO pet_pals_admin;

