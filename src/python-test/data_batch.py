import mysql.connector



cnx = mysql.connector.connect(user='oucru', password='vitrygtr',
                              host='localhost',
                              database='seqbox')


sql_select_query = """ SELECT `id_batch`, `name_batch` FROM `batch` WHERE 1"""

cursor = cnx.cursor()

result = cursor.execute(sql_select_query)

print("Selection reussie des exemples ... - OK - ")
records = cursor.fetchall()
print(records)


cnx.close()