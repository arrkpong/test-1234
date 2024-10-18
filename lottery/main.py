import sqlite3

# เชื่อมต่อหรือสร้างฐานข้อมูล orders.db
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# สร้างตาราง Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(100)
)
''')

# สร้างตาราง Orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    number VARCHAR(10),
    type VARCHAR(20),
    bet_amount INTEGER,
    reward_amount INTEGER,
    total_amount INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
)
''')

# ใส่ข้อมูลตัวอย่าง
cursor.execute("INSERT INTO Users (username) VALUES ('zzz')")
cursor.execute("INSERT INTO Orders (user_id, number, type, bet_amount, reward_amount, total_amount) VALUES (1, '55', '2 บน', 5, 500, 42)")

# บันทึกการเปลี่ยนแปลง
conn.commit()

# ดึงข้อมูลจากฐานข้อมูล
cursor.execute("SELECT * FROM Orders")
orders = cursor.fetchall()

# แสดงผลข้อมูล
for order in orders:
    print(order)

# ปิดการเชื่อมต่อฐานข้อมูล
conn.close()
