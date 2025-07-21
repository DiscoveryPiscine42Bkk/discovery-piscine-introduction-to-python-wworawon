#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้าง array ใหม่โดยเพิ่ม +2 ถ้า num > 5
new_array = [num + 2 for num in original_array if num > 5]

# แสดงผล array เดิม
print(original_array)

# แสดงผลแบบ set (ลบ duplicates)
print(set(new_array))
