import mysql.connector

#connect to the server
cnx = mysql.connector.connect(
    port = 3306,
    user = "root",
    password = "password",
    database = "user_profiles"
)

#get a cursor
cur = cnx.cursor()

#execute a query
print(cur.execute("SELECT id FROM something"))

