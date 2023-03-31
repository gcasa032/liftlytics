-- Cross field validation for age
SELECT 
  a1.name, 
  a1.sex,
  a1.meetname AS meet_name_1,
  a2.meetname AS meet_name_2,
  a1.federation as fed1,
  a2.federation as fed2, 
  a1.age AS age1,
  a2.age AS age2, 
  a1.date AS date1, 
  a2.date AS date2
FROM "liftlytics"."openpowerlifting-meet-data" a1
JOIN "liftlytics"."openpowerlifting-meet-data" a2 ON a1.name = a2.name AND a1.sex = a2.sex
WHERE a1.date < a2.date 
  AND (a2.age - a1.age) <> (CAST(DATE_FORMAT(FROM_ISO8601_DATE(a2.date), '%Y') AS int) - CAST(DATE_FORMAT(FROM_ISO8601_DATE(a1.date), '%Y') AS int))
  and abs((a2.age - a1.age) - (CAST(DATE_FORMAT(FROM_ISO8601_DATE(a2.date), '%Y') AS int) - CAST(DATE_FORMAT(FROM_ISO8601_DATE(a1.date), '%Y') AS int))) > 1
ORDER BY a1.name, a1.date, a2.date;
