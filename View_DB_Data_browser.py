from flask import Flask,request,jsonify
import logging
import mysql.connector as conn

logging.basicConfig(filename='browser.log',level=logging.DEBUG,format="%(asctime)s,%(levelname)s,%(message)s")

app=Flask(__name__)

try:
    mydb=conn.connect(host="localhost",user="root",passwd="ar@66007")
    logging.info('We are successfully connected with db %s',mydb)
except Exception as e:
    logging.exception(e)

cursor=mydb.cursor()

@app.route('/display')

def display_data():
    try:
        db_name=request.args.get('db_name')
        table_name=request.args.get('table_name')
        cursor.execute('use {}'.format(db_name))
        cursor.execute('select * from {}'.format(table_name))
        data=cursor.fetchall()
        return jsonify(str(data))
    except Exception as e:
        logging.exception(e)

if __name__=='__main__':
    app.run(port=5003)
