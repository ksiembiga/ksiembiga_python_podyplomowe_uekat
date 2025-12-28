import pytest
import math


def prime_test(n: int) -> bool:
    if n <= 1:
        return False

    elif n == 2:
        return True

    elif n % 2 == 0:
        return False


    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
            if n % i == 0:
                return False
    return True


try:
    print(prime_test(2))
    print(prime_test(3))
    print(prime_test(4))
    print(prime_test(0))
    print(prime_test(1))
    print(prime_test(5))
    print(prime_test(97))
finally:
    pass