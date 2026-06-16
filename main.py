# ตัวแปรทั่วโลกเก็บรายชื่องาน
tasks = []
task_id_counter = 0


def add_task():
    """เพิ่มงานใหม่"""
    global task_id_counter
    
    print("\n" + "-"*30)
    print("เพิ่มงานใหม่")
    print("-"*30)
    
    # ขอข้อมูลจากผู้ใช้
    title = input("ป้อนชื่อเรื่อง: ").strip()
    if not title:
        print("⚠️  ชื่อเรื่องต้องไม่ว่าง!")
        return
    
    description = input("ป้อนรายละเอียด: ").strip()
    due_date = input("ป้อนวันครบกำหนด (dd/mm/yyyy): ").strip()
    
    # สร้าง dictionary สำหรับงานใหม่
    task_id_counter += 1
    new_task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    
    # เพิ่มงานลงใน list
    tasks.append(new_task)
    print(f"\n✅ เพิ่มงาน '{title}' สำเร็จแล้ว (ID: {task_id_counter})")


def view_all_tasks():
    """ดูงานทั้งหมด"""
    print("\n" + "-"*80)
    print("รายการงานทั้งหมด")
    print("-"*80)
    
    # ตรวจสอบว่ามีงานหรือไม่
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        print("-"*80)
        return
    
    # แสดงหัวตาราง
    print(f"{'ลำดับ':<5} {'ชื่องาน':<30} {'วันครบกำหนด':<15} {'สถานะ':<15}")
    print("-"*80)
    
    # แสดงแต่ละงาน
    for index, task in enumerate(tasks, 1):
        status = "✅ เสร็จแล้ว" if task["completed"] else "⏳ ยังไม่เสร็จ"
        print(f"{index:<5} {task['title']:<30} {task['due_date']:<15} {status:<15}")
    
    print("-"*80)


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
