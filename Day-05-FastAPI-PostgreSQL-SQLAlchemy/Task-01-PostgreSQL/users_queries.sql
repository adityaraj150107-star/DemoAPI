-- Day 05 / Task 1: PostgreSQL database and SQL CRUD practice
-- Create database demoapi_day5 in pgAdmin first.
-- Then open Query Tool for demoapi_day5 and run this complete script.
--
-- This users table intentionally matches the SQLAlchemy User model
-- used in Task 2, so both tasks can use the same database and table.

CREATE TABLE IF NOT EXISTS users (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) NOT NULL UNIQUE,
    age         INTEGER CHECK (age IS NULL OR age BETWEEN 0 AND 120),
    is_active   BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- INSERT: sample records. Safe to rerun because email is unique.
INSERT INTO users (name, email, age, is_active)
VALUES
    ('Aditya Raj', 'aditya.day5@example.com', 21, TRUE),
    ('Hemang Joshi', 'hemang.day5@example.com', 22, TRUE),
    ('Demo User', 'demo.day5@example.com', 20, FALSE)
ON CONFLICT (email) DO NOTHING;

-- 1. Display all users
SELECT * FROM users ORDER BY id;

-- 2. Display only active users
SELECT * FROM users WHERE is_active = TRUE;

-- 3. Find a user by email
SELECT * FROM users WHERE email = 'aditya.day5@example.com';

-- 4. Sort users by age (youngest first)
SELECT * FROM users ORDER BY age ASC;

-- 5. Update a user's age
UPDATE users
SET age = 23
WHERE email = 'demo.day5@example.com';

-- Verify the updated record
SELECT * FROM users WHERE email = 'demo.day5@example.com';

-- 6. Count total users
SELECT COUNT(*) AS total_users FROM users;

-- 7. Count users by active status
SELECT is_active, COUNT(*) AS user_count
FROM users
GROUP BY is_active
ORDER BY is_active DESC;

-- 8. Delete the demo record (uncomment to practice DELETE)
-- DELETE FROM users WHERE email = 'demo.day5@example.com';

-- 9. Verify final table data
SELECT * FROM users ORDER BY id;
