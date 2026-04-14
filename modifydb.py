import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# ---------- CREATE TABLES ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mobile TEXT UNIQUE,
    email TEXT,
    aadhar TEXT,
    role TEXT,
    trust INTEGER DEFAULT 80
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    location TEXT,
    rent INTEGER,
    owner TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER,
    consumer TEXT,
    owner TEXT,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()

# ---------- USERS ----------
def add_user(name, mobile, email, aadhar, role):
    cursor.execute("""
    INSERT INTO users (name, mobile, email, aadhar, role, trust)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name.strip(), mobile.strip(), email.strip(), aadhar.strip(), role, 80))
    conn.commit()

def get_user_by_mobile(mobile):
    cursor.execute("SELECT * FROM users WHERE mobile=?", (mobile,))
    row = cursor.fetchone()
    return dict(row) if row else None

def update_trust(name, points):
    cursor.execute("""
    UPDATE users SET trust = MIN(MAX(trust + ?, 0), 100)
    WHERE name=?
    """, (points, name))
    conn.commit()

# ---------- ITEMS ----------
def add_item(name, category, location, rent, owner):
    cursor.execute("""
    INSERT INTO items (name, category, location, rent, owner)
    VALUES (?, ?, ?, ?, ?)
    """, (name.strip(), category, location, rent, owner))
    conn.commit()

def get_items():
    cursor.execute("SELECT * FROM items")
    return [dict(row) for row in cursor.fetchall()]

# ---------- REQUESTS ----------
def add_request(item_id, consumer, owner):
    cursor.execute("""
    SELECT * FROM requests 
    WHERE item_id=? AND consumer=? AND status='Pending'
    """, (item_id, consumer))
    
    if cursor.fetchone():
        return False

    cursor.execute("""
    INSERT INTO requests (item_id, consumer, owner, status)
    VALUES (?, ?, ?, 'Pending')
    """, (item_id, consumer, owner))
    
    conn.commit()
    return True

def get_requests_for_user(username):
    cursor.execute("""
    SELECT r.id, r.status, r.consumer, r.owner,
           i.name, i.category, i.location, i.rent
    FROM requests r
    JOIN items i ON r.item_id = i.id
    WHERE r.owner=? OR r.consumer=?
    """, (username, username))
    
    return [dict(row) for row in cursor.fetchall()]

def update_request_status(request_id, status):
    cursor.execute("UPDATE requests SET status=? WHERE id=?", (status, request_id))
    conn.commit()