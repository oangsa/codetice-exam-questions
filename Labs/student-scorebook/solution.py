student_count = int(input())
records = []
total_sum = 0.0
top_name = ""
top_total = -1.0

for _ in range(student_count):
    name = input().strip()
    homework = float(input())
    midterm = float(input())
    final = float(input())
    total = homework + midterm + final

    if total >= 80:
        grade = "A"
    elif total >= 70:
        grade = "B"
    elif total >= 60:
        grade = "C"
    elif total >= 50:
        grade = "D"
    else:
        grade = "F"

    records.append((name, total, grade))
    total_sum += total
    if total > top_total:
        top_name = name
        top_total = total

print("Score Report:")
for name, total, grade in records:
    print(f"{name}: {total:.2f} ({grade})")
print(f"Average: {total_sum / student_count:.2f}")
print(f"Top Student: {top_name} {top_total:.2f}")
