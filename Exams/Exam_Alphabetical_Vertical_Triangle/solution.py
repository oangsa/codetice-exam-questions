def letter(n):
    if n < 26:
        return chr(ord("a") + n)

    return chr(ord("A") + n - 26)


def main():
    size = int(input())
    triangle = [[""] * size for _ in range(size)]
    k = 0

    for col in range(size):
        for row in range(col, size):
            triangle[row][col] = letter(k)
            k += 1

    for row in range(size):
        print(" ".join(triangle[row][:row + 1]))


if __name__ == "__main__":
    main()
