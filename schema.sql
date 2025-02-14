-- schema.sql

-- Table: staff
CREATE TABLE IF NOT EXISTS staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    gender TEXT NOT NULL,
    dob TEXT NOT NULL,
    street TEXT NOT NULL,
    locality TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    hiring_date TEXT NOT NULL,
    salary REAL NOT NULL
);

-- Table: flight
CREATE TABLE IF NOT EXISTS flight (
    flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    departure_time TEXT NOT NULL,
    duration TEXT NOT NULL
);

-- Table: user
CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    gender TEXT NOT NULL,
    email TEXT NOT NULL,
    language TEXT,
    nationality TEXT,
    dob TEXT,
    street TEXT,
    locality TEXT,
    city TEXT,
    country TEXT,
    phone TEXT
);

-- Table: ticket
CREATE TABLE IF NOT EXISTS ticket (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_id INTEGER NOT NULL,
    passenger_id INTEGER NOT NULL,
    seat_no TEXT NOT NULL,
    date_of_journey TEXT NOT NULL,
    flight_class TEXT NOT NULL,
    fare REAL NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (flight_id) REFERENCES flight (flight_id),
    FOREIGN KEY (passenger_id) REFERENCES passenger (passenger_id)
);

-- Table: passenger
CREATE TABLE IF NOT EXISTS passenger (
    passenger_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (user_id)
);

-- Table: refunds
CREATE TABLE IF NOT EXISTS refunds (
    refund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES ticket (ticket_id)
);

-- Table: message
CREATE TABLE IF NOT EXISTS message (
    message_id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_email TEXT NOT NULL,
    message_author TEXT NOT NULL,
    author_country TEXT NOT NULL,
    message TEXT NOT NULL,
    message_of_review TEXT NOT NULL
);