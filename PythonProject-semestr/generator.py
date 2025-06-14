def is_prime(n: int) -> bool:
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def prime_generator(start: int, end: int):
    return (n for n in range(start, end + 1) if is_prime(n))
