
--SELECT <columns // *>
--FROM <tbale>
--WHERE <READ CONSTRAINS>
--ORDER <> LIMIT <>


--Read all columns

-- SELECT * FROM student

--Read only name and email

-- SELECT name,email from student;

-- SELECT * FROM student
-- WHERE email = 'john@gmail.com'
-- OR
-- email = 'delillah@gmail.com'

-- SELECT * from student
-- WHERE pocket_money > 50
-- AND pocket_money < 100

SELECT * from student
ORDER BY name ASC
LIMIT 2