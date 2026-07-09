# Alphabetical Vertical Triangle

**Difficulty:** Hard

## Problem

จงเขียนโปรแกรมภาษา Python เพื่อสร้าง `Alphabetical Vertical Triangle` ตามขนาดที่ผู้ใช้ป้อน

ก่อนอื่นให้พิจารณา `Numeric Triangle` ที่เรียงตัวเลขเพิ่มขึ้นจากซ้ายไปขวาในแต่ละแถว เช่น เมื่อ `Size = 3`

```text
1
2 3
4 5 6
```

ตัวเลขเริ่มจาก `1` และเพิ่มทีละ `1` จากซ้ายไปขวา เมื่อครบจำนวนของแถวนั้นแล้วจึงขึ้นแถวใหม่

แต่ `Numeric Vertical Triangle` จะเรียงลำดับจากบนลงล่างในแต่ละ column ก่อน แล้วจึงเลื่อนไป column ถัดไป เช่น เมื่อ `Size = 3`

```text
1
2 4
3 5 6
```

ให้นำลำดับแบบ `Numeric Vertical Triangle` มาใช้กับตัวอักษรภาษาอังกฤษ โดยเริ่มจากตัวพิมพ์เล็ก `a` ถึง `z` จากนั้นถ้าเกิน `z` ให้เปลี่ยนเป็นตัวพิมพ์ใหญ่ เริ่มจาก `A`

ตัวอย่างเมื่อ `Size = 3`

```text
a
b d
c e f
```

ตัวอย่างเมื่อ `Size = 8`

```text
a
b i
c j p
d k q v
e l r w A
f m s x B E
g n t y C F H
h o u z D G I J
```

## Input

จำนวนเต็มบวก `N` จำนวน 1 ค่า

กำหนดให้:

- `1 <= N <= 9`

## Output

แสดง `Alphabetical Vertical Triangle` ขนาด `N`

แต่ละแถวให้คั่นตัวอักษรด้วยช่องว่าง 1 ช่อง และต้องไม่มีช่องว่างต่อท้ายบรรทัด

# Hint
- ord() และ chr() ทำอะไรได้น้าาา
