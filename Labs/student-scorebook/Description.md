# Student Scorebook

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อสรุปคะแนนนักเรียน

นักเรียนแต่ละคนมีคะแนน 3 ส่วนคือ homework, midterm, final และ total คือผลรวมของคะแนนทั้ง 3 ส่วน

Grade ใช้เงื่อนไขนี้:

- `A` เมื่อ total ตั้งแต่ `80` ขึ้นไป
- `B` เมื่อ total ตั้งแต่ `70` ถึงน้อยกว่า `80`
- `C` เมื่อ total ตั้งแต่ `60` ถึงน้อยกว่า `70`
- `D` เมื่อ total ตั้งแต่ `50` ถึงน้อยกว่า `60`
- `F` เมื่อ total น้อยกว่า `50`

## Input

บรรทัดแรกเป็นจำนวนเต็ม `N` แทนจำนวนนักเรียน

นักเรียนแต่ละคนใช้ข้อมูล 4 บรรทัด:

1. name
2. homework score
3. midterm score
4. final score

## Output

แสดง report ตามรูปแบบ:

```text
Score Report:
<name>: <total> (<grade>)
Average: <average>
Top Student: <name> <total>
```

คะแนนทั้งหมดต้องแสดงทศนิยม 2 ตำแหน่ง
