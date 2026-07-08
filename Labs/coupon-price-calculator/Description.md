# Coupon Price Calculator

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อคำนวณยอดซื้อสินค้าและ coupon

Coupon ที่รองรับ:

- `SAVE10`: ลดราคา `10%` จาก subtotal
- `SAVE50`: ลดราคา `50` Baht เฉพาะเมื่อ subtotal ตั้งแต่ `300` Baht ขึ้นไป
- `FREESHIP`: ค่าส่งเป็น `0` Baht
- `NONE`: ไม่มีส่วนลด

Shipping fee ปกติคือ `40` Baht แต่ถ้า subtotal ตั้งแต่ `500` Baht ขึ้นไป ให้ shipping เป็น `0` Baht

## Input

บรรทัดแรกเป็นจำนวนเต็ม `N` แทนจำนวน item

อีก `N` บรรทัดถัดมาเป็นข้อมูล item ในรูปแบบ `<name> <price> <qty>` โดย name ไม่มีช่องว่าง

บรรทัดสุดท้ายเป็น coupon code

## Output

แสดงผล 4 บรรทัด:

```text
Subtotal: <subtotal> Baht
Discount: <discount> Baht
Shipping: <shipping> Baht
Total: <total> Baht
```

จำนวนเงินต้องแสดงทศนิยม 2 ตำแหน่ง
