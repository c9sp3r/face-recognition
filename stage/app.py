from flask import Flask,request,render_template
from csv import reader
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")
database={'skander':'skander','james':'aac','karthik':'asdsf'}


@app.route('/logout',methods=['GET'])
def logout():
    return render_template('index.html')
    

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('index.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('index.html',info='Invalid Password')
        else:
	    #return render_template('trash.html',name=name1)
            f= open('C:/Users/skand/Documents/projet/Attendance.csv','r')
            b=reader(f)
            header='''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CSV Viewer with HTML, CSS & JavaScript</title>
        <style media="screen">
          table {
  border-collapse: collapse;
  border-radius: 5px;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.25);
  overflow: hidden;
  font-family: "Quicksand", sans-serif;
  font-weight: bold;
  font-size: 14px;
  margin: auto;
}

th {
  background: #009578;
  color: #ffffff;
  text-align: left;
}

th,
td {
  padding: 10px 20px;
}

tr:nth-child(even) {
  background: #eeeeee;
}

        </style>
    </head>
    <body>

        <table id="csvRoot">'''
            c=False
            for x in b:
                header+="<tr>"
                for y in x:
                    h="<td>" if c else "<th>"
                    hh="</td>" if c else "</th>"
                    header+=h+y+hh
                c=True
                header+="</tr>"
            return header+"</table> <button onclick='window.location.href=\"/logout\"'>Logout</button></body></html>"
if __name__ == '__main__':
    app.run()
