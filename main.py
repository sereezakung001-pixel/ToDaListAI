print("Hello World")
def add_task():
    """เพิ่มงานใหม่"""
    pass


def view_all_tasks():
    """ดูงานทั้งหมด"""
    pass


def edit_task():
    """แก้ไขงาน"""
    pass


def delete_task():
    """ลบงาน"""
    pass


def show_menu():
    """แสดงเมนูหลัก"""
    print("\n" + "="*30)
    print("     เมนู To-Do List")
    print("="*30)
    print("1. เพิ่มงานใหม่")
    print("2. ดูงานทั้งหมด")
    print("3. แก้ไขงาน")
    print("4. ลบงาน")
    print("5. ออกจากโปรแกรม")
    print("="*30)


def main():
    """ฟังก์ชันหลัก"""
    while True:
        show_menu()
        choice = input("เลือกตัวเลือก (1-5): ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("ออกจากโปรแกรม... ลาก่อน!")
            break
        else:
            print("โปรดเลือกตัวเลือกที่ถูกต้อง (1-5)")


if __name__ == "__main__":
    main()
