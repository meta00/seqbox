
import mysql.connector
import datetime



cnx = mysql.connector.connect(user='oucru', password='vitrygtr',
                              host='localhost',
                              database='seqbox')

     
now = datetime.datetime.now()
formatted_time = now.strftime('%m-%d-%y %H:%M:%S')
print ('La date de la connexion :',formatted_time)



cnx.close()
