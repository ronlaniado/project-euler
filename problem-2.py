def fib(max):
    sum = 2
    prev = 1
    curr = 2

    while (curr <= max):
        new = prev + curr
        prev = curr
        curr = new
        print("prev:", prev, "curr:", curr, "new:", new, "sum:", sum)

        if (curr % 2 == 0):
            sum += curr


fib(4_000_000)
