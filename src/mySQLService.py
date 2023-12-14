import mysql.connector

class MySQLService:
  def __init__(self):
    self.host = 'localhost'
    self.user = 'root'
    self.password = 'password'
    self.database = 'portfoliodatabase'

  def connect(self):
    connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
    return connection.cursor()

  def getStatistics(self, business_id: str):
    cursor = self.connect()
    query = f'SELECT * FROM business WHERE business_id = {business_id}'
    cursor.execute(query)
    return cursor.fetchall()