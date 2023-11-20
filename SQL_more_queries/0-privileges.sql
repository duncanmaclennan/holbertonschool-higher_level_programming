-- privilages
-- Save this as 0-privileges.sql

-- For user 'user_0d_1'
SELECT CONCAT('Grants for ', user, '@', host, ':') AS 'User',
       GROUP_CONCAT(DISTINCT CONCAT(permission_type, ' ON ', db_name, '.', table_name) SEPARATOR '; ') AS 'Privileges'
FROM
    (SELECT user, host, db AS db_name, table_name, column_priv AS permission_type
     FROM mysql.columns_priv
     WHERE user='user_0d_1' AND host='localhost'
     UNION
     SELECT user, host, db AS db_name, table_name, table_priv AS permission_type
     FROM mysql.tables_priv
     WHERE user='user_0d_1' AND host='localhost'
     UNION
     SELECT user, host, db AS db_name, '' AS table_name, Db_priv AS permission_type
     FROM mysql.db
     WHERE user='user_0d_1' AND host='localhost'
     UNION
     SELECT user, host, '' AS db_name, '' AS table_name, Global_priv AS permission_type
     FROM mysql.user
     WHERE user='user_0d_1' AND host='localhost') AS privileges_info
GROUP BY user, host;

-- For user 'user_0d_2'
SELECT CONCAT('Grants for ', user, '@', host, ':') AS 'User',
       GROUP_CONCAT(DISTINCT CONCAT(permission_type, ' ON ', db_name, '.', table_name) SEPARATOR '; ') AS 'Privileges'
FROM
    (SELECT user, host, db AS db_name, table_name, column_priv AS permission_type
     FROM mysql.columns_priv
     WHERE user='user_0d_2' AND host='localhost'
     UNION
     SELECT user, host, db AS db_name, table_name, table_priv AS permission_type
     FROM mysql.tables_priv
     WHERE user='user_0d_2' AND host='localhost'
     UNION
     SELECT user, host, db AS db_name, '' AS table_name, Db_priv AS permission_type
     FROM mysql.db
     WHERE user='user_0d_2' AND host='localhost'
     UNION
     SELECT user, host, '' AS db_name, '' AS table_name, Global_priv AS permission_type
     FROM mysql.user
     WHERE user='user_0d_2' AND host='localhost') AS privileges_info
GROUP BY user, host;
