from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

# Flask App Initialization
app = Flask(__name__)

# Secret key for flash messages
app.secret_key = "your_secret_key"

# Database connection
connection = pymysql.connect(
    host='anish107.mysql.pythonanywhere-services.com',
    user='anish107',  
    password='Airlinesmanagement',  
    database='anish107$default',  
    cursorclass=pymysql.cursors.DictCursor  
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin/admin-panel')
def admin_panel():
    return render_template('admin/admin-panel.html')

# Staff Management

@app.route('/admin/staff-management', methods=['GET'])
def staff_management():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM staff")
            staff_list = cursor.fetchall()
        return render_template('admin/staff-management.html', staff_list=staff_list)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('admin_panel'))

@app.route('/admin/add-staff', methods=['POST'])
def add_staff():
    try:
        data = request.form
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO staff (name, surname, gender, dob, street, locality, city, country, phone, email, hiring_date, salary) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (data['name'], data['surname'], data['gender'], data['dob'], data['street'], data['locality'], 
                  data['city'], data['country'], data['phone'], data['email'], data['hiring_date'], data['salary']))
        connection.commit()
        flash("Staff added successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('staff_management'))

@app.route('/admin/remove-staff', methods=['POST'])
def remove_staff():
    try:
        staff_id = request.form['staff_id']
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM staff WHERE staff_id = %s", (staff_id,))
        connection.commit()
        flash("Staff removed successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('staff_management'))

@app.route('/admin/search-staff', methods=['GET'])
def search_staff():
    staff_id = request.args.get('staff_id')
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM staff WHERE staff_id = %s", (staff_id,))
            staff = cursor.fetchone()
        return render_template('admin/staff-management.html', staff_list=[staff] if staff else [])
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('staff_management'))


# Flight Management
@app.route('/admin/flight-management', methods=['GET', 'POST'])
def flight_management():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM flight")
            flights = cursor.fetchall()
        return render_template('admin/flight-management.html', flights=flights)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('admin_panel'))

@app.route('/admin/add-flight', methods=['POST'])
def add_flight():
    try:
        source = request.form['source']
        destination = request.form['destination']
        departure_time = request.form['departure_time']
        duration = request.form['duration']
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO flight (source, destination, departure_time, duration) VALUES (%s, %s, %s, %s)",
                (source, destination, departure_time, duration)
            )
        connection.commit()
        flash("Flight added successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('flight_management'))

@app.route('/admin/remove-flight', methods=['POST'])
def remove_flight():
    try:
        flight_id = request.form['flight_id']
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM flight WHERE flight_id = %s", (flight_id,))
        connection.commit()
        flash("Flight removed successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('flight_management'))

@app.route('/admin/modify-flight', methods=['POST'])
def modify_flight():
    try:
        flight_id = request.form['flight_id']
        source = request.form['source']
        destination = request.form['destination']
        departure_time = request.form['departure_time']
        duration = request.form['duration']
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE flight 
                SET source = %s, destination = %s, departure_time = %s, duration = %s 
                WHERE flight_id = %s
            """, (source, destination, departure_time, duration, flight_id))
        connection.commit()
        flash("Flight modified successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('flight_management'))

@app.route('/admin/search-flight', methods=['GET'])
def search_flight():
    flight_id = request.args.get('flight_id')
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM flight WHERE flight_id = %s", (flight_id,))
            flight = cursor.fetchone()
        return render_template('admin/flight-management.html', flights=[flight] if flight else [])
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('flight_management'))

# Refund Management
@app.route('/admin/refund-management')
def refund_management():
    return render_template('admin/refund-management.html')

# User Management

@app.route('/admin/user-management', methods=['GET'])
def user_management():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user")
            users = cursor.fetchall()
        return render_template('admin/user-management.html', users=users)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('admin_panel'))

@app.route('/admin/add-user', methods=['POST'])
def add_user():
    try:
        data = request.form
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO user (name, surname, gender, email, nationality, dob)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (data['name'], data['surname'], data['gender'], data['email'], data['nationality'], data['dob']))
        connection.commit()
        flash("User added successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('user_management'))

@app.route('/admin/remove-user', methods=['POST'])
def remove_user():
    try:
        user_id = request.form['user_id']
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM user WHERE user_id = %s", (user_id,))
        connection.commit()
        flash("User removed successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('user_management'))


# Ticket Management

@app.route('/admin/ticket-management')
def ticket_management():
    return render_template('admin/ticket-management.html')

@app.route('/user/user-panel')
def user_panel():
    return render_template('user/user-panel.html')

@app.route('/user/check-flights')
def check_flights():
    return render_template('user/check-flights.html')

@app.route('/user/book-ticket')
def book_ticket():
    return render_template('user/book-ticket.html')

@app.route('/user/cancel-ticket')
def cancel_ticket():
    return render_template('user/cancel-ticket.html')

@app.route('/user/about-us')
def about_us():
    return render_template('user/about-us.html')

@app.route('/user/contact-us')
def contact_us():
    return render_template('user/contact-us.html')

if __name__ == '__main__':
    app.run(debug=True)
