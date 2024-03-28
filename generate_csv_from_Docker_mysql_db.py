import mysql.connector
import csv

db = mysql.connector.connect(
  user="root",
  password="mysql",
  host="localhost",
  port="13306"
)
cursor = db.cursor()
cursor.execute("SELECT * FROM rin_db.users")

with open('rin_db_users.csv','w',newline='') as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writerow([i[0] for i in cursor.description])
  csvwriter.writerows(cursor)

print("csv safely generated.")
