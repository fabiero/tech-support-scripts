-- SQL Day 1 & 2 Practice Queries
-- Created by Frida

-- Basic SELECT
SELECT * FROM users;
SELECT name, email FROM users;

-- Filtering
SELECT * FROM users WHERE status = 'active';
SELECT * FROM users WHERE status = 'active' AND city = 'Nairobi';
SELECT * FROM users WHERE city = 'Mombasa' OR city = 'Kisumu';
SELECT * FROM users WHERE NOT status = 'active';
SELECT * FROM users WHERE id BETWEEN 2 AND 4;
SELECT * FROM users WHERE email LIKE '%gmail%';

-- Sorting & Limiting
SELECT * FROM users ORDER BY name;
SELECT * FROM users ORDER BY name DESC;
SELECT * FROM users LIMIT 3;

-- JOIN
SELECT users.name, tickets.issue, tickets.priority, tickets.status
FROM tickets
JOIN users ON tickets.user_id = users.id;

SELECT users.name, tickets.issue, tickets.status
FROM tickets
JOIN users ON tickets.user_id = users.id
WHERE tickets.status = 'open';

-- Aggregations
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM tickets WHERE status = 'open';
SELECT priority, COUNT(*) FROM tickets GROUP BY priority;
SELECT status, COUNT(*) as total FROM tickets GROUP BY status ORDER BY total DESC;

-- GROUP BY + HAVING
SELECT priority, COUNT(*) as total
FROM tickets
GROUP BY priority
HAVING COUNT(*) > 1;

-- JOIN + GROUP BY
SELECT users.name, COUNT(tickets.id) as total_tickets
FROM users
JOIN tickets ON users.id = tickets.user_id
GROUP BY users.name;
