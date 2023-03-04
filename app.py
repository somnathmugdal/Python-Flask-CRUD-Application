# Required Libraries
from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
from logger import log

#Flask App Setup
log("crud","PYTHON FLASK CRUD APPLICATION")
app = Flask(__name__)
app.secret_key = 'many random bytes'

#Database Credentials
host = 'localhost'
username = 'root'
password = 'somnath'
log("crud",f"Database Credentials \n Host : {host}\t Username : {username}\t Password : {password}\t")

#App Conifg
app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = username
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = 'crud'
log("crud",f"Database Configured Sucessfully") 

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    log("crud","Home Page Loaded Sucessfully !")
    log("crud",f"{data}")
    return render_template('index.html', students=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        log("crud","Data Inserted Successfully !")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        log("crud",f"Insert Query : \n INSERT INTO students (name, email, phone) VALUES (%s, %s, %s), (name, email, phone)")
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    log("crud","Data Deleted Successfully !")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))



@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE students SET name=%s, email=%s, phone=%s
        WHERE id=%s
        """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        log("crud","Data updated Successfully !")
        return redirect(url_for('Index'))




if __name__ == "__main__":
    app.run(debug=True)