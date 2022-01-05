import random


def fermat_test(p: int) -> bool:
    """Fast checks if x is probably prime by using a Fermat's little theorem method"""
    assert p > 1, "Exponent value must be upper 1"

    a = random.randint(2, 10)
    while a >= p and a % p == 0:
        a = random.randint(2, 10)

    return a ** (p - 1) % p == 1


def is_prime(x: int) -> bool:
    """Slow checks if x is prime by using a sequential enumeration of divisors
    from 2 to sqrt(x) method"""
    divider = 2
    while divider < x ** 0.5:
        if x % divider == 0:
            return False
        divider += 1
    return True


def generate_odd_random_number(min_v: int, max_v: int) -> int:
    x = random.randint(min_v, max_v)
    while x % 2 == 0:
        x = random.randint(min_v, max_v)
    return x


def generate_prime(min_v: int, max_v: int) -> int:
    assert isinstance(min_v, int) and min_v > 0, "Wrong begin number of the range"
    assert isinstance(max_v, int) and max_v > min_v, "Wrong end number of the range"

    verified_prime = False
    probably_prime = False

    while not verified_prime:
        while not probably_prime:
            x = generate_odd_random_number(min_v, max_v)
            probably_prime = True
            print("Checking at Fermat's algorithm: ", x)
            for i in range(2):
                probably_prime *= fermat_test(x)
                print(f"Test {i}", " Success!" if probably_prime else "Fail")

        print("Final full checking: ", x)
        verified_prime = is_prime(x)

    return x


MinValue = 1_000_000
MaxValue = 6_500_000
print(generate_prime(MinValue, MaxValue), " is prime")
