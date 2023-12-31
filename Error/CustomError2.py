class UncountableError(ValueError):
    def __init__(self, wrong_value):
        super().__init__(f"Invalid value for n, {wrong_value}. n must be greater than 0.")
        self.wrong_value = wrong_value


def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)


if __name__ == "__main__":
    count_from_zero_to_n(0)
