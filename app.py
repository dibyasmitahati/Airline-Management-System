from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin/admin-panel')
def admin_panel():
    return render_template('admin/admin-panel.html')

@app.route('/admin/staff-management')
def staff_management():
    return render_template('admin/staff-management.html')

@app.route('/admin/flight-management')
def flight_management():
    return render_template('admin/flight-management.html')

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
