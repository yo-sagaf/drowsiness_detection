import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host='localhost',
  user='setsisuser',
  passwd='setsis0809',
  database='SETSISBASE'
)

mycursor = mydb.cursor()
val='PersonDetect'
conf='fgdfgdfgdf'
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')


#sql = "INSERT INTO EVENTS(Name,Date) VALUE( \" "+ val+" \", \" " +formatted_date+"," " \" )"
sql = "INSERT INTO EVENTS(Name,Date,Confidence) VALUE( \" "+ val+" \", \" " +formatted_date+ " \", \" "+conf+ " \"  )"

print(sql)
mycursor.execute(sql)
#mycursor.execute(sql2)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
