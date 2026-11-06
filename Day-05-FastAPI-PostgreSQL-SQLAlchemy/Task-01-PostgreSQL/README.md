# Task 1 — PostgreSQL

## Objective
Practice PostgreSQL database and table creation, inserting records, reading data, updating records, deleting records, filtering, sorting, and aggregate queries.

## Steps

1. Open pgAdmin 4 and connect to your local PostgreSQL server.
2. Create a database named `demoapi_day5`.
3. Open Query Tool for that database.
4. Open `users_queries.sql`, execute the script, and inspect the result grid.
5. Run the SELECT statements individually to capture screenshots of the output.

## What the SQL file demonstrates

- CREATE DATABASE (run separately if needed), CREATE TABLE
- INSERT, SELECT, UPDATE, DELETE
- WHERE, ORDER BY, LIMIT
- COUNT and GROUP BY

## Note
The SQL script assumes you have already created and connected to `demoapi_day5`. PostgreSQL server must be running. The script uses `CREATE TABLE IF NOT EXISTS`; the sample inserts are safe to rerun because email is unique and uses `ON CONFLICT`.
