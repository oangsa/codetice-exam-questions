def calculate_grade(score):
    if score >= 80: return 'A'
    elif score >= 70: return 'B'
    elif score >= 60: return 'C'
    elif score >= 50: return 'D'
    else: return 'F'

def main():
    n = int(input().strip())
    for _ in range(n):
        parts = input().strip().split()
        if len(parts) == 2:
            name, score = parts[0], int(parts[1])
            print(f"{name} {calculate_grade(score)}")

if __name__ == '__main__':
    main()
