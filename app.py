from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

# Flask App Initialization
app = Flask(__name__)

# Secret key for flash messages
app.secret_key = "your_secret_key"

# Database connection
connection = pymysql.connect(
    host='localhost',
    user='root',  # Replace with your MySQL username
    password='JustInTime321',  # Replace with your MySQL password
    database='airlinez_test',  # Replace with your database name
    cursorclass=pymysql.cursors.DictCursor  # Return results as dictionaries
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin/admin-panel')
def admin_panel():
    return render_template('admin/admin-panel.html')

@app.route('/admin/staff-management')
def staff_management():
    return render_template('admin/staff-management.html')

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

@app.route('/admin/user-management')
def user_management():
    return render_template('admin/user-management.html')

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
