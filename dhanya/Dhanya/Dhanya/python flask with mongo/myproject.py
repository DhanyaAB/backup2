from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017", connect=False)
db = client.mymongodb2
employee = db.employees


@app.route("/")
def add_emp():
    return render_template('insert.html')


@app.route("/employee", methods=['POST'])
def emp_insert():
    if request.method == 'POST':
        ename = request.form['ename']
        esal = request.form['esal']
        eid = request.form['eid']
        employee = db.employees.insert({"ename": str(ename), "esal": str(esal), "eid": str(eid)})
        res = db.employees.find()
        result = []
        for data in res:
            result.append(data)
    return render_template('showdb.html', result=result)


@app.route("/employees", methods=['GET'])
def get_employee():
    try:
        res = db.employees.find()
    except Exception as e:
        return str(e), 200

    return render_template('showdb.html', result=res)


@app.route("/employees/<int:eid>")
def get_by_id(eid):
    eid = eid
    res = employee.find({"eid": str(eid)})
    result = []
    for data in res:
        result.append(data)
    return render_template('showid.html', result=result)


@app.route("/employees/delete/<int:eid>")
def delete_by_id(eid):
    eid = eid
    employee = db.employees.remove({"eid": str(eid)})
    res = db.employees.find()
    result = []
    for data in res:
        result.append(data)
    return render_template('showdb.html', result=result)


@app.route("/employees/update/<int:eid>")
def update_emp(eid):
    eid = eid
    res = employee.find({"eid": str(eid)})
    keys = []
    values = []
    for data in res:
        for key, value in data.items():
            keys.append(key)
            values.append(value)
    return render_template('edit.html', keys=keys, values=values)



@app.route("/employees/updated", methods = ['POST'])
def update_by_id():
    if request.method == 'POST':
        ename = request.form['ename']
        esal = request.form['esal']
        eid = request.form['eid']
        employee = db.employees.update({"eid": str(eid)}, {'$set': {"ename": str(ename), "esal": str(esal), "eid": str(eid)}})
        res = db.employees.find()
        result = []
        for data in res:
            result.append(data)
    return render_template('showdb.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
