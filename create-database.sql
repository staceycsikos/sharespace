CREATE DATABASE sharespace;

CREATE USER sharespace_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE sharespace TO sharespace_admin;
