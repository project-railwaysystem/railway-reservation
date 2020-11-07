from flask import Flask, render_template,request
import mysql.connector

app = Flask(__name__, static_url_path="", static_folder="static")

from flaskext.mysql import MySQL
try:
   mysql = MySQL()
   app.config['MYSQL_DATABASE_USER'] ="id15343073_railway"
   app.config['MYSQL_DATABASE_PASSWORD'] = "[%!|O)uhs*73veLk"
   app.config['MYSQL_DATABASE_DB'] ="id15343073_railway_reservation"
   app.config['MYSQL_DATABASE_HOST'] = "localhost"
   mysql.init_app(app)
   con=mysql.connect()
   cursor=con.cursor()
except Exception as e:
   print("Error while connecting to MySQL", e)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store',methods=['POST', 'GET'])
def store():
   if request.method=='POST':
      try:
         fname=request.form['fname']
         lname=request.form['lname']
         from1=request.form['from1']
         to1=request.form['to1']
         date=request.form['date']
         type1=request.form['type1']
         count=request.form['count']
         class1=request.form['class1']
         email=request.form['email']
         tel=request.form['tel']
         payment=request.form['payment']
         if(cursor.execute('''insert into railway (fname,lname,from1,to1,date,type1,count,class1,email,tel,payment) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(fname,lname,from1,to1,date,type1,count,class1,email,tel,payment))): 
            con.commit()
            return render_template('index.html',response = 'Ticked Booked Sucessfully')
         else:
            return render_template('index.html',response = 'Something Wrong')
      except Exception as e:
         return render_template('index.html',response = 'Something Wrong')
   else:
      return render_template('index.html',response = 'Something Wrong')

if __name__ == "__main__":
    app.run()
