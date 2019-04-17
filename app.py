from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)
@app.route('/',methods=['POST', 'GET'])
def home():
   return render_template('default.html')

@app.route('/postadd',methods=['POST', 'GET'])
def postadd():
    if request.method == 'POST':
        try:
            name = str(request.form['name'])
            date = str(request.form['date'])
            time = str(request.form['time'])
            con = sql.connect("college.db")
            cur = con.cursor()
            cur.execute("INSERT INTO lab VALUES (?,?,?)", (name, date,time))
            con.commit()
            print("ADDEDEEDDEED")
        except:
            con.rollback()
        finally:
            return render_template("default.html")
            con.close()


@app.route('/addtable',methods=['POST', 'GET'])
def datadisplay():
    return render_template('add_details.html')


@app.route('/display', methods=['POST', 'GET'])
def display():
   if request.method == 'POST':
      try:
          con = sql.connect("college.db")
          con.row_factory = sql.Row
          cur = con.cursor()
          cur.execute("select * from lab")
          rows = cur.fetchall();
      except:
         con.rollback()
         msg = "Login Error"
      finally:
            print(rows)
            return render_template("displaytable.html", rows=rows)
            con.close()


if __name__ == '__main__':
   app.run(debug=True)
