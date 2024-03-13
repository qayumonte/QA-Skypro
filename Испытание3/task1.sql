SELECT DISTINCT d.name AS destination_name
FROM Destination d
JOIN Tickets t ON d.id = t.id_destination;

SELECT DISTINCT d.name AS destination_name
FROM Destination d
JOIN Tickets t ON d.id = t.id_destination
JOIN Status s ON d.id_status = s.id
WHERE s.name = 'Без визы';

SELECT d.name AS destination_name,
       GREATEST(t.lowest_price, t.highest_price) AS highest_price
FROM Destination d
JOIN Tickets t ON d.id = t.id_destination
WHERE GREATEST(t.lowest_price, t.highest_price) > (
       SELECT AVG((lowest_price + highest_price) / 2)
       FROM Tickets
);

SELECT DISTINCT class_name
FROM visits;

SELECT u.user_surname, u.user_name, SUM(v.hours_spent) AS total_hours_spent
FROM user u
JOIN visits v ON u.id_user = v.id_user
GROUP BY u.user_surname, u.user_name;

SELECT AVG(u.age) AS average_age
FROM user u
JOIN visits v ON u.id_user = v.id_user
WHERE v.class_name = 'Flex';

SELECT DISTINCT title
FROM book
WHERE year_publish > '1990-01-01';

SELECT a.full_name AS author_name,
       SUM(b.pages) AS total_pages
FROM author a
JOIN book b ON a.id = b.id_author
GROUP BY a.full_name;

SELECT CAST((year_publish / 100) + 1 AS INTEGER) AS century,
       COUNT(*) AS book_count
FROM book
GROUP BY century
ORDER BY century;
