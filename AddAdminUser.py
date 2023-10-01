import sqlite3

# สร้างหรือเชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect('pos_database.db')
cursor = conn.cursor()

# สร้างตารางสำหรับเก็บข้อมูลผู้ใช้
cursor.execute(''' CREATE TABLE IF NOT EXISTS users (
               username TEXT PRIMARY KEY,
               password TEXT
            )''')

# เพิ่มข้อมูลผู้ใช้ admin
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('admin', 'password123'))

# บันทึกการเปลื่ยนเปลงและปิดการเชื่อมต่อ
conn.commit()
conn.close()