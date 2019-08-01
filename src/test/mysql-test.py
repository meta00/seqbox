from flask import Flask, render_template
import mysql.connector


app = Flask(__name__)




cnx = mysql.connector.connect(user='oucru', password='vitrygtr',
                              host='localhost',
                              database='seqbox')


sql_select_query = """ SELECT id_sample, num_seq FROM `sample` WHERE 1"""

cursor = cnx.cursor()

result = cursor.execute(sql_select_query)


records = cursor.fetchall()

@app.route('/') 
def sample(): 
    return render_template('sample.html',title='Sample') 
    
if __name__ == '__main__': 
    app.run()



