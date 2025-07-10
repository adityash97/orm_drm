-- SQLite
-- select four_rating, three_rating from (select Count(id) as four_rating from testApp_rating
-- where testApp_rating.rating = 4,
-- select Count(id) as three_rating from testApp_rating
-- where testApp_rating.rating = 3)

-- select testApp_restaurant.id,testApp_restaurant.name from testApp_restaurant;


-- SELECT
--     COUNT(CASE WHEN rating = 4 THEN 1 END) AS four_rating,
--     COUNT(CASE WHEN rating = 3 THEN 1 END) AS three_rating
-- FROM testApp_rating;


-- select restaurant_id, 
-- CASE rating
-- when 4 then 'good rest'
-- when 3 then 'avg rest'
-- else 'bad rest' END
-- from testApp_rating;



-- SELECT restaurant_id,
--     CASE WHEN rating = 4 THEN  "Good Rest",
--     CASE WHEN rating = 3 THEN  "Avg Rest",
--     CASE WHEN rating < 3 THEN  "bad Rest" END AS rating_label
-- FROM testApp_rating;


-- SELECT restaurant_id,
--     CASE 
--     WHEN rating = 4 THEN  "Good Rest",
--     WHEN rating = 3 THEN  "Avg Rest",
--     WHEN rating < 3 THEN  "bad Rest" END AS rating_label
-- FROM testApp_rating;


-- update testApp_restaurant
-- set website = NULL where id = 10

select restaurant_id, avg(income)as avg_income from testApp_sale group by restaurant_id


SELECT testApp_restaurant.name,testApp_rating.restaurant_id,avg(testApp_rating.rating) as avg_rating from testApp_rating

 join testApp_restaurant
on testApp_restaurant.id = testApp_rating.restaurant_id
group by testApp_rating.restaurant_id


select testApp_restaurant.name,testApp_rating.restaurant_id,count(testApp_rating.rating) from testApp_rating
join testApp_restaurant 
on testApp_restaurant.id = testApp_rating.restaurant_id

group by restaurant_id



select  restaurant_restaurant.name,  Avg(restaurant_rating.rating) as avg_rating from 
restaurant_restaurant join restaurant_rating on  restaurant_restaurant.id = restaurant_rating.restaurant_id
group by restaurant_restaurant.name having restaurant_restaurant.id = 31

select rating from restaurant_rating where id= 32



select * from restaurant_restaurant
-- select  testApp_books.author_id,count(id) as Books_Count  from testApp_books group by testApp_books.author_id 