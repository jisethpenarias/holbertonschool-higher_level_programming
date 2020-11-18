--  lists all cities contained in the database hbtn_0d_usa.

SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities 
    LEFT JOIN hbtn_0d_usa.states ON cities.state_id = states.id
ORDER BY cities.id ASC
