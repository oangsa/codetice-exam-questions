# Library Borrowing System

**Difficulty:** Medium

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อจำลองระบบยืม-คืนหนังสือใน library

หนังสือแต่ละเล่มมี `book_code`, `title`, และจำนวน copies ที่ available

Command ที่รองรับ:

- `BORROW <member> <book_code>` ยืมหนังสือถ้ามี copies เหลือ
- `RETURN <member> <book_code>` คืนหนังสือ ถ้า member เคยยืม book code นั้นไว้
- `STATUS` แสดงจำนวน copies ที่ available ของหนังสือทุกเล่ม เรียงตาม book code

## Input

บรรทัดแรกเป็นจำนวนเต็ม `B` แทนจำนวนหนังสือ

อีก `B` บรรทัดถัดมาเป็นข้อมูลหนังสือในรูปแบบ `<book_code> <title> <copies>` โดย title ไม่มีช่องว่าง

บรรทัดถัดมาเป็นจำนวนเต็ม `N` แทนจำนวน command

อีก `N` บรรทัดถัดมาเป็น command บรรทัดละ 1 command

## Output

ให้แสดงผลตาม command ที่ทำ
