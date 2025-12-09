def total(a, b, possible_sum):
    return a + b == possible_sum


num_1 = input("Enter an integer: ")
num_2 = input("Enter another integer: ")
possible_total = input("Enter their sum: ")
print(f"{num_1} + {num_2} {"equals" if total(num_1, num_2, possible_total) else "does not equal"} {possible_total}")
