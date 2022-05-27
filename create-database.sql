CREATE DATABASE sharespace;

CREATE USER share_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE sharespace TO share_admin;