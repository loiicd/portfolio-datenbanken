import mysql.connector

class MySQLService:
  def __init__(self):
    self.host = 'localhost'
    self.user = 'root'
    self.password = 'password'
    self.database = 'portfoliodatabase'

  def connect(self):
    try:
      return  mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
    except mysql.connector.Error as err:
      raise Exception(f'Error: {err}')

  def getStatistics(self, business_id: str):
    try:
      connection = self.connect()
      cursor = connection.cursor()
      query = f'SELECT * FROM business WHERE business_id = {business_id}'
      cursor.execute(query)
      return cursor.fetchone()
    except Exception as err:
      return err
    finally:
      connection.close()