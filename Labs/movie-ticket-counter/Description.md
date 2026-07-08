# Movie Ticket Counter

**Difficulty:** Medium

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อจำลอง ticket counter ของโรงหนัง

Ticket type และราคา:

- `CHILD`: 80 Baht
- `ADULT`: 120 Baht
- `SENIOR`: 90 Baht
- `VIP`: 250 Baht

ถ้า request ทำให้จำนวน ticket sold เกิน seat limit ให้ปฏิเสธ request นั้นและไม่เพิ่ม revenue

## Input

บรรทัดแรกเป็น movie name

บรรทัดที่สองเป็น seat limit

บรรทัดที่สามเป็นจำนวนเต็ม `N` แทนจำนวน request

อีก `N` บรรทัดถัดมาเป็น request ในรูปแบบ `<customer> <ticket_type> <qty>`

## Output

แสดงผลแต่ละ request และ summary หลังจบทั้งหมด
