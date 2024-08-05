def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

def test_fibonacci():
    for i in range(1, 11):
        print(f"Fibonacci sequence of length {i}: {fibonacci(i)}")

if __name__ == "__main__":
    num = int(input("Enter the length of the Fibonacci sequence: "))
    print(f"Fibonacci sequence of length {num}: {fibonacci(num)}")
    test_fibonacci()
