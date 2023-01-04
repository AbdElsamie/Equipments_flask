
import pymysql
from flask import flash, redirect, render_template, request

from app import app
from db_config import mysql
from tables import Results

# from fpdf import FPDF #pip install fpdf


@app.route('/')
def main():
    return render_template('equip.html')


@app.route('/new_equipment')
def add_Equipment_view():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_user():
    conn = None
    cursor = None
    try:
        _name_equipment = request.form['name_equipment']
        _type_equipment = request.form['type_equipment']
        _make_country = request.form['make_country']
        _price = request.form['price']
        _purpose = request.form['purpose']
        _trainer = request.form['trainer_name']
        _class_name = request.form['class_name']
        _room = request.form['room']
        _time_of_class = request.form['time_of_class']
        # validate the received values
        if _name_equipment and _type_equipment and _make_country and _price and _purpose and _trainer and _class_name and _room and _time_of_class and request.method == 'POST':
            # same tables
            sql = "INSERT INTO equipment_table (name_equipment, type_equipment, make_country, price, purpose , trainer_name ,class_name , room ,time_of_class ) VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s )"
            data = (_name_equipment, _type_equipment, _make_country, _price,
                    _purpose, _trainer, _class_name, _room, _time_of_class)  # same tables
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Equipment added successfully!')
            return redirect('/')
        else:
            return 'Error while adding equipment'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/main')
def main_page():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM equipment_table")
        rows = cursor.fetchall()
        table = Results(rows)
        table.border = True
        return render_template('equipments.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit/<int:id>')
def edit_equipment(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM equipment_table WHERE id=%s", (id))
        row = cursor.fetchone()
        if row:
            return render_template('edit.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['POST'])
def update_user():
    conn = None
    cursor = None
    try:
        _name_equipment = request.form['name_equipment']
        _type_equipment = request.form['type_equipment']
        _make_country = request.form['make_country']
        _price = request.form['price']
        _purpose = request.form['purpose']
        _trainer = request.form['trainer_name']
        _class_name = request.form['class_name']
        _room = request.form['room']
        _time_of_class = request.form['time_of_class']
        _id = request.form['id']
        # validate the received values
        if _name_equipment and _type_equipment and _make_country and _price and _purpose and _trainer and _class_name and _room and _time_of_class and request.method == 'POST':

            sql = "UPDATE equipment_table SET name_equipment=%s, type_equipment=%s, make_country=%s, price=%s, purpose=%s , trainer_name=%s ,class_name=%s  , room=%s ,time_of_class=%s  WHERE id=%s"
            data = (_name_equipment, _type_equipment, _make_country, _price, _purpose,
                    _trainer, _class_name, _room, _time_of_class,  _id)  # same tables
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Equipment updated successfully!')
            return redirect('/')
        else:
            return 'Error while updating equipment'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/<int:id>')
def delete_equipment(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipment_table WHERE id=%s", (id,))
        conn.commit()
        flash('equipment deleted successfully!')
        return redirect('/')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()
"""import pymysql
from flask import flash, redirect, render_template, request

from app import app
from db_config import mysql
from tables import Results

# from fpdf import FPDF #pip install fpdf


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/new_equipment')
def add_Equipment_view():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_user():
    conn = None
    cursor = None
    try:
        _name_equipment = request.form['name_equipment']
        _type_equipment = request.form['type_equipment']
        _make_country = request.form['make_country']
        _price = request.form['price']
        _purpose = request.form['purpose']
        _trainer = request.form['trainer_name']
        _class_name = request.form['class_name']
        _room = request.form['room']
        _time_of_class = request.form['time_of_class']
        # validate the received values
        if _name_equipment and _type_equipment and _make_country and _price and _purpose and _trainer and _class_name and _room and _time_of_class and request.method == 'POST':

            # same tables
            sql = "INSERT INTO equipment_table (name_equipment, type_equipment, make_country, price, purpose , trainer_name ,class_name , room ,time_of_class ) VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s )"
            data = (_name_equipment, _type_equipment, _make_country, _price,
                    _purpose, _trainer, _class_name, _room, _time_of_class)  # same tables
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Equipment added successfully!')
            return redirect('/')
        else:
            return 'Error while adding equipment'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/main')
def main_page():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM equipment_table")
        rows = cursor.fetchall()
        table = Results(rows)
        table.border = True
        return render_template('equipments.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit/<int:id>')
def edit_equipment(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM equipment_table WHERE id=%s", (id))
        row = cursor.fetchone()
        if row:
            return render_template('edit.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['POST'])
def update_user():
    conn = None
    cursor = None
    try:
        _name_equipment = request.form['name_equipment']
        _type_equipment = request.form['type_equipment']
        _make_country = request.form['make_country']
        _price = request.form['price']
        _purpose = request.form['purpose']
        _trainer = request.form['trainer_name']
        _class_name = request.form['class_name']
        _room = request.form['room']
        _time_of_class = request.form['time_of_class']
        _id = request.form['id']
        # validate the received values
        if _name_equipment and _type_equipment and _make_country and _price and _purpose and _trainer and _class_name and _room and _time_of_class and request.method == 'POST':

            sql = "UPDATE equipment_table SET name_equipment=%s, type_equipment=%s, make_country=%s, price=%s, purpose=%s , trainer_name=%s ,class_name=%s  , room=%s ,time_of_class=%s  WHERE id=%s"
            data = (_name_equipment, _type_equipment, _make_country, _price, _purpose,
                    _trainer, _class_name, _room, _time_of_class,  _id)  # same tables
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Equipment updated successfully!')
            return redirect('/')
        else:
            return 'Error while updating equipment'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/<int:id>')
def delete_equipment(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipment_table WHERE id=%s", (id,))
        conn.commit()
        flash('equipment deleted successfully!')
        return redirect('/')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()"""
