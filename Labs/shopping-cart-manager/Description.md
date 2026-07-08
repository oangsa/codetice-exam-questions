# Shopping Cart Manager

**Difficulty:** Hard

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อจัดการ shopping cart อย่างง่าย

ระบบมี product เริ่มต้น โดยแต่ละ product มี `product_id`, `name`, `price`, และ `stock`

Command ที่รองรับ:

- `ADD <product_id> <qty>` เพิ่มสินค้าเข้า cart ถ้า stock พอ
- `REMOVE <product_id> <qty>` นำสินค้าออกจาก cart และคืน stock
- `VIEW` แสดงรายการใน cart และ total

ถ้า total ก่อนลดราคาเกิน `1000` Baht ให้ลดราคา `10%` ตอนแสดง `VIEW`

## Input

บรรทัดแรกเป็นจำนวนเต็ม `P` แทนจำนวน product

อีก `P` บรรทัดถัดมาเป็นข้อมูล product ในรูปแบบ `<product_id> <name> <price> <stock>`

บรรทัดถัดมาเป็นจำนวนเต็ม `N` แทนจำนวน command

อีก `N` บรรทัดถัดมาเป็น command บรรทัดละ 1 command

## Output

ให้แสดงผลตาม command ที่ทำ จำนวนเงินต้องแสดงทศนิยม 2 ตำแหน่ง
