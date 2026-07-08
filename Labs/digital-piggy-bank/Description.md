# Digital Piggy Bank

**Difficulty:** Easy

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อจำลอง piggy bank ของผู้ใช้ 1 คน

piggy bank เริ่มต้นด้วย balance `0.00` Baht และรองรับ command ต่อไปนี้:

- `DEPOSIT <amount>` เพิ่มเงินเข้า balance
- `WITHDRAW <amount>` ถอนเงินออกจาก balance ถ้าเงินพอ
- `CHECK` แสดง balance ปัจจุบัน

## Input

บรรทัดแรกเป็น owner name

บรรทัดที่สองเป็นจำนวนเต็ม `N` แทนจำนวน command

อีก `N` บรรทัดถัดมาเป็น command บรรทัดละ 1 command

## Output

เมื่อ `DEPOSIT` สำเร็จ ให้แสดง:

```text
Deposited <amount> Baht to <owner>. Balance: <balance> Baht.
```

เมื่อ `WITHDRAW` สำเร็จ ให้แสดง:

```text
Withdrew <amount> Baht from <owner>. Balance: <balance> Baht.
```

ถ้าเงินไม่พอ ให้แสดง:

```text
Failed: Insufficient funds in <owner>'s piggy bank.
```

เมื่อเจอ `CHECK` ให้แสดง:

```text
Balance for <owner>: <balance> Baht.
```

หลังจากทำครบทุก command ให้แสดง:

```text
Final Balance: <balance> Baht
```

จำนวนเงินต้องแสดงทศนิยม 2 ตำแหน่ง
