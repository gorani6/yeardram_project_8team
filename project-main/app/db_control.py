import os
import pymysql


class DB:
    host = 'mysql'
    port = 3306
    user = os.getenv('DB_USER')
    pwd = os.getenv('DB_PW')
    dbname = os.getenv('DB_NAME')

    ### default functions
    def db_connect(self):
        con = pymysql.Connect(
            host=self.host, port=self.port,\
            user=self.user, password=self.pwd, database=self.dbname)
        return con

    def check_connection(self):
        try: 
            con = self.db_connect()
            con.close()
            return 'success'
        except: return f'failed: {self.host} {self.user} {self.pwd} {self.dbname}'
    
    ### create table functions
    def create_table(self, table_name, col_data_type):
        try:
            con = self.db_connect()
            cur = con.cursor()
            cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({col_data_type})")
            con.commit()
            con.close()
            return 'success'
        except: return 'failed'
    
    ### delete, drop functions
    def delete_table(self, table_name):
        try:
            con = self.db_connect()
            cur = con.cursor()
            cur.execute(f"DELETE FROM f{table_name}")
            con.commit()
            con.close()
            return 'success'
        except: return 'failed'

    ### update functions
    ### insert functions