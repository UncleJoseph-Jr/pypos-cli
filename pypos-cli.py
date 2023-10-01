import sqlite3

from categories import CategoryManager

category_manager = CategoryManager()

def login(username, password):
    conn = sqlite3.connect('pos_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return True
    else:
        return False
    
# ตัวอย่างการใช้งาน
# username = input("กรอกชื่อผู้ใช้: ")
# password = input("กรอกรหัสผ่าน: ")

# if login(username, password):
#     print("เข้าสู่ระบบสำเร็จ!")
# else:
#     print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

def login_system():
    while True:
        username = input("กรอกชื่อผู้ใช้: ")
        password = input("กรอกรหัสผ่าน: ")

        if login(username, password):
            print("เข้าสู่ระบบสำเร็จ!")
            break
        else:
            print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

login_system()

def main_menu():
    while True:
        print("\nเมนูหลัก: ")
        print("1. เปิดบิล")
        print("2. จัดการสินค้า")
        print("3. จัดการหมวดหมูสินค้า")
        print("0. ออกจากระบบ")

        choice = input("เลือกเมนู: ")

        if choice == '1':
            # เรียกฟังก์ชั่นเปิดบิล
            perform_sales()
        elif choice == '2':
            # เรียกฟังก์ชั่นจัดการสินค้า
            manage_product()
        elif choice == '3':
            # เรียกฟังก์ชั่นจัดการหมวดหมูสินค้า
            manage_categories()
        elif choice == '0':
            print("exit")
            break
        else:
            print("กรุณาเลือกหมายเลขที่ถูกต้อง")

main_menu()

def manage_categories():
    while True:
        print("\nเมนูจัดการหมวดหมู่:")
        print("1. เพิ่มหมวดหมู่")
        print("2. แก้ไขหมวดหมู่")
        print("3. แสดงหมวดหมู่ทั้งหมด")
        print("4. กลับสู่เมนูหลัก")

        choice = input("กรุณาเลือกหมายเลขเมนู: ")

        if choice == '1':
            name = input("กรอกชื่อหมวดหมู่ใหม่: ")
            category_manager.add_category(name)
            print("เพิ่มหมวดหมู่สำเร็จ!")
        elif choice == '2':
            category_id = int(input("กรอรหัสหมวดหมู่ที่ต้องกสรแก้ไข: "))
            new_name = input("กรอกชื่อหมวดหมู่ใหม่; ")
            category_manager.edit_category(category_id= new_name)
            print("แก้ไขหมวดหมู่สำเร็จ!")
        elif choice == '3':
            categories = category_manager.get_all_categories()
            print("\nรายชื่อหมวดหมู่ทั้งหมด: ")
            for category in categories:
                print(f"{categories.category_id}. {category.name}")
        elif choice == '0':
            print("กลับสู่เมนูหลัก")
            break
        else:
            print("กรุณาเลือกหมายเลขที่ถูกต้อง")
manage_categories()