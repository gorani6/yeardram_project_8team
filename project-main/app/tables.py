from db_control import DB

# create_table(table_name, col and its data type query)
example = 'id int, name varchar(32)'
DB().create_table('table123', example)