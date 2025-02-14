# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Flask App Initialization
app = Flask(__name__)

# Secret key for session management and flash messages
app.secret_key = "your_secret_key"

# SQLite Database connection
DATABASE = 'airlinez_test.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

# Index Page
@app.route('/')
def index():
    return render_template('index.html')

# Admin Section

# Admin Login Page
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'JustInTime321':  # Hardcoded password for admin
            session['admin_logged_in'] = True
            flash("Login successful!", "success")
            return redirect(url_for('admin_panel'))
        else:
            flash("Invalid password!", "danger")
    return render_template('admin/admin-login.html')

# Admin Panel (Protected Route)
@app.route('/admin/admin-panel')
def admin_panel():
    if not session.get('admin_logged_in'):
        flash("You need to login first!", "warning")
        return redirect(url_for('admin_login'))
    return render_template('admin/admin-panel.html')

# Logout Route
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash("You have been logged out!", "success")
    return redirect(url_for('admin_login'))

# Before Request Handler to Protect Admin Routes
@app.before_request
def require_login():
    admin_routes = [
        'admin_panel', 'staff_management', 'add_staff', 'remove_staff', 'modify_staff_form', 'modify_staff', 'search_staff',
        'flight_management', 'add_flight', 'remove_flight', 'modify_flight', 'search_flight',
        'refund_management', 'get_refunds', 'clear_refund', 'decline_refund', 'report_fraud',
        'user_management', 'add_user', 'remove_user',
        'ticket_management', 'remove_ticket', 'search_ticket', 'modify_ticket', 'add_ticket',
        'feedback_management'
    ]
    if request.endpoint in admin_routes and not session.get('admin_logged_in'):
        flash("You need to login first!", "warning")
        return redirect(url_for('admin_login'))

# Staff Management

# Page Rendering
@app.route('/admin/staff-management', methods=['GET'])
def staff_management():
    try:
        conn = get_db_connection()
        staff_list = conn.execute('SELECT * FROM staff ORDER BY staff_id').fetchall()
        conn.close()
        return render_template('admin/staff-management.html', staff_list=staff_list)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('admin_panel'))

# Add Staff
@app.route('/admin/add-staff', methods=['POST'])
def add_staff():
    try:
        data = request.form
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO staff (name, surname, gender, dob, street, locality, city, country, phone, email, hiring_date, salary) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (data['name'], data['surname'], data['gender'], data['dob'], data['street'], data['locality'], 
              data['city'], data['country'], data['phone'], data['email'], data['hiring_date'], data['salary']))
        conn.commit()
        conn.close()
        flash("Staff added successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('staff_management'))

# Remove Staff
@app.route('/admin/remove-staff', methods=['POST'])
def remove_staff():
    try:
        staff_id = request.form['staff_id']
        conn = get_db_connection()
        conn.execute("DELETE FROM staff WHERE staff_id = ?", (staff_id,))
        conn.commit()
        conn.close()
        flash("Staff removed successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('staff_management'))

# Modify Staff
@app.route('/admin/modify-staff/<int:staff_id>', methods=['GET'])
def modify_staff_form(staff_id):
    try:
        conn = get_db_connection()
        staff = conn.execute("SELECT * FROM staff WHERE staff_id = ?", (staff_id,)).fetchone()
        conn.close()
        if staff:
            return render_template('admin/staff-management.html', staff=staff)
        else:
            flash("Staff not found", "danger")
            return redirect(url_for('staff_management'))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('staff_management'))

@app.route('/admin/modify-staff', methods=['POST'])
def modify_staff():
    try:
        data = request.form
        conn = get_db_connection()
        conn.execute("""
            UPDATE staff
            SET name = ?, surname = ?, gender = ?, dob = ?, street = ?,
                locality = ?, city = ?, country = ?, phone = ?, email = ?,
                hiring_date = ?, salary = ?
            WHERE staff_id = ?
        """, (data['name'], data['surname'], data['gender'], data['dob'], data['street'], data['locality'], 
              data['city'], data['country'], data['phone'], data['email'], data['hiring_date'], data['salary'], data['staff_id']))
        conn.commit()
        conn.close()
        flash("Staff modified successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('staff_management'))

# Search Staff
@app.route('/admin/search-staff', methods=['GET'])
def search_staff():
    staff_id = request.args.get('staff_id')
    try:
        conn = get_db_connection()
        staff = conn.execute("SELECT * FROM staff WHERE staff_id = ?", (staff_id,)).fetchone()
        conn.close()
        return render_template('admin/staff-management.html', staff_list=[staff] if staff else [])
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('staff_management'))

# Flight Management

# Page Rendering
@app.route('/admin/flight-management', methods=['GET', 'POST'])
def flight_management():
    try:
        conn = get_db_connection()
        flights = conn.execute("SELECT * FROM flight").fetchall()
        conn.close()
        return render_template('admin/flight-management.html', flights=flights)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('admin_panel'))

# Add Flight
@app.route('/admin/add-flight', methods=['POST'])
def add_flight():
    try:
        data = request.form
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO flight (source, destination, departure_time, duration) 
            VALUES (?, ?, ?, ?)
        """, (data['source'], data['destination'], data['departure_time'], data['duration']))
        conn.commit()
        conn.close()
        flash("Flight added successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('flight_management'))

# Remove Flight
@app.route('/admin/remove-flight', methods=['POST'])
def remove_flight():
    try:
        flight_id = request.form['flight_id']
        conn = get_db_connection()
        conn.execute("DELETE FROM flight WHERE flight_id = ?", (flight_id,))
        conn.commit()
        conn.close()
        flash("Flight removed successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('flight_management'))

# Modify Flight
@app.route('/admin/modify-flight', methods=['POST'])
def modify_flight():
    try:
        data = request.form
        conn = get_db_connection()
        conn.execute("""
            UPDATE flight
            SET source = ?, destination = ?, departure_time = ?, duration = ?
            WHERE flight_id = ?
        """, (data['source'], data['destination'], data['departure_time'], data['duration'], data['flight_id']))
        conn.commit()
        conn.close()
        flash("Flight modified successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('flight_management'))

# Search Flight
@app.route('/admin/search-flight', methods=['GET'])
def search_flight():
    flight_id = request.args.get('flight_id')
    try:
        conn = get_db_connection()
        flight = conn.execute("SELECT * FROM flight WHERE flight_id = ?", (flight_id,)).fetchone()
        conn.close()
        return render_template('admin/flight-management.html', flights=[flight] if flight else [])
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('flight_management'))

# Refund Management

# Page Rendering
@app.route('/admin/refund-management')
def refund_management():
    return render_template('admin/refund-management.html')

# Show Refunds
@app.route('/admin/get-refunds', methods=['GET'])
def get_refunds():
    try:
        conn = get_db_connection()
        refunds = conn.execute("SELECT * FROM refunds").fetchall()
        conn.close()
        return jsonify(refunds)
    except Exception as e:
        print(f"Error fetching refunds: {e}")
        return jsonify([])

# Clear Refund
@app.route('/admin/clear-refund', methods=['POST'])
def clear_refund():
    try:
        refund_id = request.form['refund_id']
        conn = get_db_connection()
        conn.execute("UPDATE refunds SET status = 'cleared' WHERE refund_id = ?", (refund_id,))
        conn.commit()
        conn.close()
        return "Refund cleared successfully"
    except Exception as e:
        print(f"Error clearing refund: {e}")
        return "Error clearing refund", 500

# Decline Refund
@app.route('/admin/decline-refund', methods=['POST'])
def decline_refund():
    try:
        refund_id = request.form['refund_id']
        conn = get_db_connection()
        conn.execute("UPDATE refunds SET status = 'declined' WHERE refund_id = ?", (refund_id,))
        conn.commit()
        conn.close()
        return "Refund declined successfully"
    except Exception as e:
        print(f"Error declining refund: {e}")
        return "Error declining refund", 500

# Report Fraud
@app.route('/admin/report-fraud', methods=['POST'])
def report_fraud():
    try:
        refund_id = request.form['refund_id']
        conn = get_db_connection()
        conn.execute("UPDATE refunds SET status = 'fraud' WHERE refund_id = ?", (refund_id,))
        conn.commit()
        conn.close()
        return "Fraud reported successfully"
    except Exception as e:
        print(f"Error reporting fraud: {e}")
        return "Error reporting fraud", 500

# User Management

# Page Rendering
@app.route('/admin/user-management', methods=['GET'])
def user_management():
    try:
        conn = get_db_connection()
        users = conn.execute("SELECT * FROM user").fetchall()
        conn.close()
        return render_template('admin/user-management.html', users=users)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('admin_panel'))

# Add User
@app.route('/admin/add-user', methods=['POST'])
def add_user():
    try:
        data = request.form
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO user (name, surname, gender, email, nationality, dob) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (data['name'], data['surname'], data['gender'], data['email'], data['nationality'], data['dob']))
        conn.commit()
        conn.close()
        flash("User added successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('user_management'))

# Remove User
@app.route('/admin/remove-user', methods=['POST'])
def remove_user():
    try:
        user_id = request.form['user_id']
        conn = get_db_connection()
        conn.execute("DELETE FROM user WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
        flash("User removed successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('user_management'))

# Ticket Management

# Page Rendering
@app.route('/admin/ticket-management')
def ticket_management():
    try:
        conn = get_db_connection()
        tickets = conn.execute("""
            SELECT ticket.ticket_id, flight.source, flight.destination, 
                   passenger.passenger_id, user.name, user.surname, 
                   ticket.date_of_journey, ticket.flight_class, ticket.fare, ticket.status
            FROM ticket
            JOIN flight ON ticket.flight_id = flight.flight_id
            JOIN passenger ON ticket.passenger_id = passenger.passenger_id
            JOIN user ON passenger.user_id = user.user_id
        """).fetchall()
        conn.close()
        return render_template('admin/ticket-management.html', tickets=tickets)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('admin_panel'))

# Remove Ticket
@app.route('/admin/remove-ticket', methods=['POST'])
def remove_ticket():
    try:
        ticket_id = request.form['ticket_id']
        conn = get_db_connection()
        conn.execute("DELETE FROM ticket WHERE ticket_id = ?", (ticket_id,))
        conn.commit()
        conn.close()
        flash("Ticket removed successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('ticket_management'))

# Search Ticket
@app.route('/admin/search-ticket', methods=['GET'])
def search_ticket():
    ticket_id = request.args.get('ticket_id')
    try:
        conn = get_db_connection()
        ticket = conn.execute("""
            SELECT ticket.ticket_id, flight.source, flight.destination, 
                   passenger.passenger_id, user.name, user.surname, 
                   ticket.date_of_journey, ticket.flight_class, ticket.fare, ticket.status
            FROM ticket
            JOIN flight ON ticket.flight_id = flight.flight_id
            JOIN passenger ON ticket.passenger_id = passenger.passenger_id
            JOIN user ON passenger.user_id = user.user_id
            WHERE ticket.ticket_id = ?
        """, (ticket_id,)).fetchone()
        conn.close()
        return render_template('admin/ticket-management.html', tickets=[ticket] if ticket else [])
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('ticket_management'))

# Modify Ticket
@app.route('/admin/modify-ticket', methods=['POST'])
def modify_ticket():
    try:
        data = request.form
        conn = get_db_connection()
        conn.execute("""
            UPDATE ticket
            SET flight_id = ?, passenger_id = ?, seat_no = ?, 
                date_of_journey = ?, flight_class = ?, fare = ?, status = ?
            WHERE ticket_id = ?
        """, (data['flight_id'], data['passenger_id'], data['seat_no'], 
              data['date_of_journey'], data['flight_class'], data['fare'], data['status'], data['ticket_id']))
        conn.commit()
        conn.close()
        flash("Ticket modified successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('ticket_management'))

# Add Ticket
@app.route('/admin/add-ticket', methods=['POST'])
def add_ticket():
    try:
        data = request.form
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO ticket (flight_id, passenger_id, seat_no, date_of_journey, flight_class, fare, status) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (data['flight_id'], data['passenger_id'], data['seat_no'], 
              data['date_of_journey'], data['flight_class'], data['fare'], data['status']))
        conn.commit()
        conn.close()
        flash("Ticket added successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('ticket_management'))

# Feedback Management

# Page Rendering
@app.route('/admin/feedback-management')
def feedback_management():
    return render_template('admin/feedback-management.html')

# Get Feedback Data
@app.route('/admin/get-feedback', methods=['GET'])
def get_feedback():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM message")
        feedback = cursor.fetchall()
        conn.close()

        # Convert database rows to JSON serializable format
        feedback_list = [
            {
                "message_id": row["message_id"], 
                "message": row["message"],
                "message_of_review": row["message_of_review"],
                "message_email": row["message_email"],
                "message_author": row["message_author"],
                "author_country": row["author_country"],
            }
            for row in feedback
        ]
        return jsonify(feedback_list)
    
    except Exception as e:
        print(f"Error fetching feedback: {e}")
        return jsonify({"error": "Failed to fetch feedback"}), 500

# Delete Feedback
@app.route('/admin/delete-feedback/<int:message_id>', methods=['POST'])
def delete_feedback(message_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM message WHERE message_id = ?", (message_id,))
        
        if cursor.rowcount == 0:  # No row found with given message_id
            conn.close()
            return jsonify({"error": "Feedback not found."}), 404  
        
        conn.commit()
        conn.close()
        return jsonify({"message": "Feedback deleted successfully."})
    
    except Exception as e:
        print(f"Error deleting feedback: {e}")
        return jsonify({"error": str(e)}), 500

# User Management

@app.route('/user/register', methods=['GET', 'POST'])
def user_register():
    return render_template('user/register.html')

# User Login (Now Just a Page)
@app.route('/user/login', methods=['GET', 'POST'])
def user_login():
    return render_template('user/login.html')

# User Logout (Redirects to Login Page)
@app.route('/user/logout')
def user_logout():
    return redirect(url_for('user_login'))

# User Panel
@app.route('/user/user-panel')
def user_panel():
    return render_template('user/user-panel.html')

# Check Flights Route (Handles Both Rendering and Searching)
@app.route('/user/check-flights', methods=['GET', 'POST'])
def check_flights():
    if request.method == 'GET':
        return render_template('user/check-flights.html')

    elif request.method == 'POST':  # Searching for flights
        try:
            data = request.get_json()
            source = data.get('source')
            destination = data.get('destination')
            departure_date = data.get('departure_date')

            if not source or not destination or not departure_date:
                return jsonify({"status": "error", "message": "Missing required fields"}), 400

            conn = get_db_connection()
            cursor = conn.execute("""
                SELECT flight_id, source, destination, departure_time, duration 
                FROM flights 
                WHERE source = ? AND destination = ? AND DATE(departure_time) = ?
            """, (source, destination, departure_date))

            flights = cursor.fetchall()
            conn.close()

            if flights:
                return jsonify({"status": "success", "flights": [dict(flight) for flight in flights]})
            else:
                return jsonify({"status": "error", "message": "No flights available for the selected route and date."}), 404
        except Exception as e:
            print(f"Error searching flights: {e}")
            return jsonify({"status": "error", "message": "An internal error occurred"}), 500

# Book Ticket
@app.route('/user/book-ticket')
def book_ticket():
    return render_template('user/book-ticket.html')

# Cancel Ticket
@app.route('/user/cancel-ticket')
def cancel_ticket():
    return render_template('user/cancel-ticket.html')

# About Us
@app.route('/user/about-us')
def about_us():
    return render_template('user/about-us.html')

# Contact Us
@app.route('/user/contact-us')
def contact_us():
    return render_template('user/contact-us.html')

# Handle Form Submission for Contact Us
@app.route('/user/contact-us', methods=['POST'])
def handle_contact():
    email = request.form.get('email')
    name = request.form.get('name')
    country = request.form.get('country')
    message = request.form.get('message')

    if not email or not name or not country or not message:
        flash("All fields are required!", "warning")
        return redirect(url_for('contact_us'))

    try:
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO message (message_email, message_author, author_country, message, message_of_review) 
            VALUES (?, ?, ?, ?, datetime('now'))
        """, (email, name, country, message))
        conn.commit()
        conn.close()
        flash("Thank you for your feedback!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('contact_us'))

if __name__ == '__main__':
    app.run(debug=True)