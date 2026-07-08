# Inventory Restock Planner

**Difficulty:** Easy

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อช่วยร้านค้าคำนวณแผน restock

สินค้าแต่ละรายการมีข้อมูล `name`, `stock`, `minimum`, และ `target`

ถ้า `stock` น้อยกว่า `minimum` ให้ order จำนวน `target - stock` units

ถ้า `stock` มากกว่าหรือเท่ากับ `minimum` ให้แสดง `OK`

## Input

บรรทัดแรกเป็นจำนวนเต็ม `N` แทนจำนวนสินค้า

อีก `N` บรรทัดถัดมาเป็นข้อมูลสินค้าในรูปแบบ `<name> <stock> <minimum> <target>`

## Output

แสดง restock report และ total units needed
