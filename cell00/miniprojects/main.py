from typing import List

class Vegetable:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

class FarmStockManager:
    def __init__(self):
        self.stock: List[Vegetable] = []

    def add_vegetable(self, name: str, quantity: int):
        for vegetable in self.stock:
            if vegetable.name.lower() == name.lower():
                vegetable.quantity += quantity
                print(f" เพิ่มสต็อก {name} อีก {quantity} กิโลกรัม (รวมเป็น {vegetable.quantity} กิโลกรัมแล้ว)")
                return
        new_veg = Vegetable(name, quantity)
        self.stock.append(new_veg)
        print(f" เพิ่ม {name} เข้าสต็อกจำนวน {quantity} กิโลกรัมแล้ว")

    def show_stock(self):
        if not self.stock:
            print("ยังไม่มีผลไม้ในสต็อก")
        else:
            print("\n รายการผลไม้ในสต็อก:")
            for i, vegetable in enumerate(self.stock, 1):
                print(f"{i}. {vegetable.name} ({vegetable.quantity} กิโลกรัม)")

    def withdraw_vegetable(self, name: str, quantity: int):
        for vegetable in self.stock:
            if vegetable.name.lower() == name.lower():
                if vegetable.quantity >= quantity:
                    vegetable.quantity -= quantity
                    print(f" เบิก {name} จำนวน {quantity} กิโลกรัมแล้ว (คงเหลือ {vegetable.quantity} กิโลกรัม)")
                    if vegetable.quantity == 0:
                        self.stock.remove(vegetable)
                    return
                else:
                    print(f" สต็อก {name} มีไม่พอ (มีแค่ {vegetable.quantity} กิโลกรัม)")
                    return
        print(f" ไม่พบ {name} ในสต็อก")

def display_menu():
    print("\n=== ระบบเช็คและจัดการสต็อกผลไม้ในฟาร์ม ===")
    print("1. เพิ่มผลไม้เข้าสต็อก")
    print("2. แสดงรายการผลไม้ในสต็อก")
    print("3. เบิกผลไม้ออกจากสต็อก")
    print("4. ออกจากโปรแกรม")

def main():
    manager = FarmStockManager()

    while True:
        display_menu()
        choice = input("เลือกเมนู (1-4): ").strip()

        if choice == "1":
            name = input("ชื่อผลไม้: ")
            try:
                qty = int(input("จำนวนกิโลกรัม: "))
                manager.add_vegetable(name, qty)
            except ValueError:
                print("ต้องกรอกตัวเลขเท่านั้นสำหรับจำนวนกิโลกรัม")
        elif choice == "2":
            manager.show_stock()
        elif choice == "3":
            name = input("ชื่อผลไม้ที่ต้องการเบิก: ")
            try:
                qty = int(input("จำนวนกิโลกรัมที่ต้องการเบิก: "))
                manager.withdraw_vegetable(name, qty)
            except ValueError:
                print("ต้องกรอกตัวเลขเท่านั้นสำหรับจำนวนกิโลกรัม")
        elif choice == "4":
            print(" ขอบคุณที่ใช้ระบบสต็อกผลไม้ในฟาร์ม")
            break
        else:
            print("กรุณาเลือกแค่ 1-4 เท่านั้น")

if __name__ == "__main__":
    main()