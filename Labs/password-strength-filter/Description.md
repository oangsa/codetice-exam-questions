# Password Strength Filter

**Difficulty:** Medium

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อตรวจสอบ password strength

Password จะถือว่า strong เมื่อผ่านเงื่อนไขทั้งหมดนี้:

1. ความยาวอย่างน้อย `8` ตัวอักษร
2. มี lowercase อย่างน้อย 1 ตัว
3. มี uppercase อย่างน้อย 1 ตัว
4. มี digit อย่างน้อย 1 ตัว
5. มี special character อย่างน้อย 1 ตัวจาก `!@#$%`

ถ้า password ไม่ผ่านหลายเงื่อนไข ให้ใช้ reason แรกตามลำดับข้างบน

## Input

บรรทัดแรกเป็นจำนวนเต็ม `N` แทนจำนวน password

อีก `N` บรรทัดถัดมาเป็น password บรรทัดละ 1 ค่า

## Output

แสดง strong password ก่อน จากนั้นแสดง weak password พร้อม reason และ summary
