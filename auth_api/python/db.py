import mysql.connector

class DBConnector(object):

   def __init__(self):
        self.dbconn = self.create_connection()

   # creats new connection, ideally on config file and hidden the settings
   def create_connection(self):
        return mysql.connector.connect(host='bootcamp-tht.sre.wize.mx',
                                         database='bootcamp_tht',
                                         user='secret',
                                         password='noPow3r')

   # For explicitly opening database connection
   def __enter__(self):
        self.dbconn = self.create_connection()
        return self.dbconn

   def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbconn.close()