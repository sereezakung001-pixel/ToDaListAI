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
    # ตรวจสอบว่ามีงานหรือไม่
    if not tasks:
        print("\n⚠️  ยังไม่มีงานในรายการ")
        return
    
    # แสดงรายการงานก่อน
    view_all_tasks()
    
    print("\n" + "-"*30)
    print("แก้ไขงาน")
    print("-"*30)
    
    # ขอ index จากผู้ใช้
    try:
        task_index = int(input("เลือกลำดับงานที่ต้องการแก้ไข: ")) - 1
        
        # ตรวจสอบ index
        if task_index < 0 or task_index >= len(tasks):
            print("⚠️  ลำดับงานไม่ถูกต้อง!")
            return
        
        selected_task = tasks[task_index]
        
        # แสดงตัวเลือกการแก้ไข
        print(f"\nกำลังแก้ไข: {selected_task['title']}")
        print("1. แก้ไขชื่องาน")
        print("2. แก้ไขรายละเอียด")
        print("3. แก้ไขวันครบกำหนด")
        print("4. เปลี่ยนสถานะ (เสร็จแล้ว/ยังไม่เสร็จ)")
        print("0. ยกเลิก")
        
        edit_choice = input("เลือกตัวเลือก (0-4): ").strip()
        
        if edit_choice == "1":
            new_title = input("ป้อนชื่องานใหม่: ").strip()
            if new_title:
                selected_task["title"] = new_title
                print("✅ แก้ไขชื่องานสำเร็จแล้ว")
            else:
                print("⚠️  ชื่องานต้องไม่ว่าง!")
        
        elif edit_choice == "2":
            new_description = input("ป้อนรายละเอียดใหม่: ").strip()
            selected_task["description"] = new_description
            print("✅ แก้ไขรายละเอียดสำเร็จแล้ว")
        
        elif edit_choice == "3":
            new_due_date = input("ป้อนวันครบกำหนดใหม่ (dd/mm/yyyy): ").strip()
            selected_task["due_date"] = new_due_date
            print("✅ แก้ไขวันครบกำหนดสำเร็จแล้ว")
        
        elif edit_choice == "4":
            selected_task["completed"] = not selected_task["completed"]
            status = "เสร็จแล้ว" if selected_task["completed"] else "ยังไม่เสร็จ"
            print(f"✅ เปลี่ยนสถานะเป็น '{status}' สำเร็จแล้ว")
        
        elif edit_choice == "0":
            print("ยกเลิกการแก้ไข")
        
        else:
            print("⚠️  ตัวเลือกไม่ถูกต้อง!")
    
    except ValueError:
        print("⚠️  โปรดป้อนตัวเลขที่ถูกต้อง!")


def delete_task():
    """ลบงาน"""
    # ตรวจสอบว่ามีงานหรือไม่
    if not tasks:
        print("\n⚠️  ยังไม่มีงานในรายการ")
        return
    
    # แสดงรายการงานก่อน
    view_all_tasks()
    
    print("\n" + "-"*30)
    print("ลบงาน")
    print("-"*30)
    
    # ขอ index จากผู้ใช้
    try:
        task_index = int(input("เลือกลำดับงานที่ต้องการลบ: ")) - 1
        
        # ตรวจสอบ index
        if task_index < 0 or task_index >= len(tasks):
            print("⚠️  ลำดับงานไม่ถูกต้อง!")
            return
        
        selected_task = tasks[task_index]
        
        # แสดงงานที่จะลบ
        print(f"\nกำลังจะลบ: {selected_task['title']}")
        print(f"รายละเอียด: {selected_task['description']}")
        
        # ขอยืนยัน
        confirm = input("ต้องการลบงานนี้จริงหรือไม่ (y/n): ").strip().lower()
        
        if confirm == "y":
            tasks.pop(task_index)
            print("✅ ลบงานสำเร็จแล้ว")
        elif confirm == "n":
            print("ยกเลิกการลบ")
        else:
            print("⚠️  โปรดป้อน y หรือ n")
    
    except ValueError:
        print("⚠️  โปรดป้อนตัวเลขที่ถูกต้อง!")


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
