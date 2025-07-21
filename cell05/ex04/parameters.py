#!/usr/bin/env python3

import sys

# นับจำนวน arguments (ลบ 1 ตัวแรกคือชื่อไฟล์)
num_params = len(sys.argv) - 1

print(f"Number of parameters: {num_params}")