def main():
    s = input().strip()
    if not s:
        return
    fruits = s.split(',')
    counts = {}
    order = []
    for f in fruits:
        if f not in counts:
            counts[f] = 0
            order.append(f)
        counts[f] += 1
    for f in order:
        print(f"{f} {counts[f]}")

if __name__ == '__main__':
    main()
