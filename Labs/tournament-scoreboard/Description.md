# Tournament Scoreboard

**Difficulty:** Hard

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อสรุป standings จากผลการแข่งขัน

แต่ละ match มี team A, score A, team B, score B

การคิด points:

- ชนะได้ `3` points
- เสมอได้ `1` point ต่อทีม
- แพ้ได้ `0` points

ให้คำนวณ goal for (`GF`), goal against, และ goal difference (`GD`)

Standings เรียงตามลำดับนี้:

1. points มากไปน้อย
2. GD มากไปน้อย
3. GF มากไปน้อย
4. team name ตามตัวอักษร

## Input

บรรทัดแรกเป็นจำนวนเต็ม `N` แทนจำนวน match

อีก `N` บรรทัดถัดมาอยู่ในรูปแบบ `<team_a> <score_a> <team_b> <score_b>`

## Output

แสดง standings ตามรูปแบบ:

```text
Standings:
<team>: <points> pts, GD <gd>, GF <gf>
```
