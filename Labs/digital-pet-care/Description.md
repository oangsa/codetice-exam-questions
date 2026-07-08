# Digital Pet Care

**Difficulty:** Medium

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อจำลอง digital pet 1 ตัว

pet เริ่มต้นด้วย hunger `30` และ energy `80`

Command ที่รองรับ:

- `FEED`: ลด hunger ลง `20` แต่ไม่ต่ำกว่า `0` และเพิ่ม energy `5` แต่ไม่เกิน `100`
- `PLAY`: ถ้า energy น้อยกว่า `20` จะเล่นไม่ได้ ถ้าเล่นได้ให้เพิ่ม hunger `15` และลด energy `25`
- `SLEEP`: เพิ่ม hunger `10` และเพิ่ม energy `40` โดยค่าทั้งสองต้องไม่เกิน `100`
- `STATUS`: แสดง status ปัจจุบัน

## Input

บรรทัดแรกเป็น pet name

บรรทัดที่สองเป็น species

บรรทัดที่สามเป็นจำนวนเต็ม `N` แทนจำนวน command

อีก `N` บรรทัดถัดมาเป็น command บรรทัดละ 1 command

## Output

ให้แสดงผลตาม command ที่ทำ และหลังจากทำครบทุก command ให้แสดง final status:

```text
Final Status: <name> the <species> - Hunger: <hunger>/100, Energy: <energy>/100
```
