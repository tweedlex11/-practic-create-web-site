def sum_numbers(a, b):
    return a + b


def convert_c_to_f(celsius):
    return celsius * 9/5 + 32


if __name__ == "__main__":
    print("Sum:", sum_numbers(2, 3))
    print("25°C =", convert_c_to_f(25), "°F")